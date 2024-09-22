from django.core.management.base import BaseCommand
from university.models import University
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# Helper function to fit scalers for university characteristics
def fit_scalers(universities):
    scalar = StandardScaler()
    encoder = OneHotEncoder()

    # Collect all IELTS, SAT, GPA, and IELTS choice values for fitting
    ielts_values = np.array([uni.ielts for uni in universities]).reshape(-1, 1)
    sat_values = np.array([uni.sat for uni in universities]).reshape(-1, 1)
    gpa_values = np.array([uni.gpa for uni in universities]).reshape(-1, 1)
    ielts_choices = np.array([uni.ielts_choice for uni in universities]).reshape(-1, 1)

    # Fit scalers and encoders
    scalar.fit(np.hstack([ielts_values, sat_values, gpa_values]))  # Fit for numeric values
    encoder.fit(ielts_choices)  # Fit for categorical values

    return scalar, encoder


# Helper function to create vectors for a specific university
def create_university_vector(university, scalar, encoder):
    # Scale numerical values
    scaled_values = scalar.transform(
        np.array([[university.ielts, university.sat, university.gpa]])
    ).flatten()

    # One-hot encode categorical values
    encoded_ielts_choice = encoder.transform(
        np.array([[university.ielts_choice]])
    ).toarray().flatten()

    # Combine all features into a single vector
    vector = np.concatenate([scaled_values, encoded_ielts_choice])
    return vector


class Command(BaseCommand):
    help = 'Uploads university vectors to Qdrant'

    def handle(self, *args, **kwargs):
        # Initialize the Qdrant client
        client = QdrantClient("localhost", port=6333)

        universities = list(University.objects.all())

        # Fit the scalers and encoders once using all university data
        scalar, encoder = fit_scalers(universities)

        # Iterate over each university and upload its vector
        for university in universities:
            try:
                vector = create_university_vector(university, scalar, encoder)
                point = PointStruct(
                    id=university.id,
                    vector=vector.tolist(),  # Convert NumPy array to list for compatibility
                    payload={"title": university.title, "uni_id": university.id}
                )
                
                # Upload the point (vector and payload) to the Qdrant collection
                client.upsert(collection_name="universities", points=[point])

            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Failed to upload vector for {university.title}: {str(e)}"))

        self.stdout.write(self.style.SUCCESS('Successfully uploaded all university vectors to Qdrant'))

