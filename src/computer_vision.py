from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import  urllib.request as urllib
import io
import os

def auth(subscription_key, endpoint):
    """Returns authenticated client"""

    client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    return client


def run_computer_vision(client, image_url):
    """Detect faces on a given image and predict peoples' age and gender"""

    fd = urllib.urlopen(img_url)
    image_file= io.BytesIO(fd.read())
    im = Image.open(image_file)

    plt.imshow(im)

    # Get current axis
    ax = plt.gca()

    print("Running...")

    features = ["faces"]
    results = client.analyze_image(img_url, features)

    if(len(results.faces)==0):
        print("Not found!")
    else:
        for face in results.faces:
            print(face)

            # Get properties
            gender= face.gender
            age= face.age
            left= face.face_rectangle.left
            top= face.face_rectangle.top
            width = face.face_rectangle.width
            height= face.face_rectangle.height

            # Annotations
            rect= patches.Rectangle((left, top), width, height, linewidth=3, edgecolor="r", facecolor="none")
            ax.add_patch(rect)
            ax.annotate(xy=(left,top-20), text="{}\n{}".format(age,gender), color="yellow",size=10, bbox=dict(boxstyle="Square", fc="gray",ec="b",lw=0.5))
        
    plt.show()


if __name__ == '__main__':
    # Insert current path
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

    # Load environment variables
    load_dotenv()

    subscription_key= os.getenv("COMPUTER_VISION_SUBSCRIPTION_KEY")
    endpoint= os.getenv("COMPUTER_VISION_ENDPOINT")
    img_url= os.getenv("IMAGE_URL")

    # Get Client
    client = auth(subscription_key=subscription_key, endpoint=endpoint)

    # Run
    run_computer_vision(client=client, image_url=image_url)

