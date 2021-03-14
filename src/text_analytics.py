from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import sys
import os

def auth(subscription_key, endpoint):
    """Returns authenticated client"""

    ta_credential = AzureKeyCredential(subscription_key)
    client = TextAnalyticsClient(endpoint=endpoint,credential=ta_credential)

    return client


def sentiment_analysis(client, documents):
    """Returns sentiment scores of the given document"""

    # API Call
    response = client.analyze_sentiment(documents=documents)[0]

    # Print Results
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))
    for idx, sentence in enumerate(response.sentences):
        print("Sentence: {}".format(sentence.text))
        print("Sentence {} sentiment: {}".format(idx + 1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
            sentence.confidence_scores.positive,
            sentence.confidence_scores.neutral,
            sentence.confidence_scores.negative,
        ))

def entity_recognition(client, documents):
    """Detecs entities in the given documents"""

    result = client.recognize_entities(documents = documents)[0]

    print("Named Entities:\n")
    for entity in result.entities:
        print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                "\n\tConfidence Score: \t", round(entity.confidence_score, 2))


if __name__ == '__main__':
    # Insert current path
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

    # Load environment variables
    load_dotenv()

    subscription_key= os.getenv("TEXT_ANALYTICS_SUBSCRIPTION_KEY")
    endpoint= os.getenv("TEXT_ANALYTICS_VISION_ENDPOINT")
    documents = [doc for doc in os.getenv("DOCUMENTS").split(",")]

    # Get Client
    client = auth(subscription_key, endpoint)

    # Run
    if os.getenv("SERVICE") == "sentiment_analysis":
        sentiment_analysis(client=client, documents=documents)
    elif os.getenv("SERVICE") == "entity_recognition":
        entity_recognition(client=client, documents=documents)
