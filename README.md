# METU Workshop Content
<div style="text-align:center"><img src="docs/images/metu.svg.png" /></div>

## Instructions

1. Install [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/download.html) 
2. Create conda environment using environment.yaml and activate it
```
conda env create --file=environment.yaml
conda activate research_venv
```
3. Use .env file to make settings (you can add .env file into .gitignore when you make the project public)

```
# Computer Vision Settings

COMPUTER_VISION_SUBSCRIPTION_KEY=your-subscription key
COMPUTER_VISION_ENDPOINT=your-endpoint
IMAGE_URL=image-url

# Text Analytics Settings

TEXT_ANALYTICS_SUBSCRIPTION_KEY=your-subscription key
TEXT_ANALYTICS_VISION_ENDPOINT=your-endpoint

DOCUMENTS=Example Sentence 1,Example 2

SERVICE=entity_recognition # Options: sentiment_analysis, entity_recognition 

```

4. Run the related script
```
python src/computer_vision.py
python src/text_analytics.py
```

## Resources

[Computer Vision Overview](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/overview)

[Computer Vision Client SDK and Rest API](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/client-library?tabs=visual-studio&pivots=programming-language-python)

[Text Analytics Overview](https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview)

[Text Analytics Client SDK and Rest API](https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/client-libraries-rest-api?tabs=version-3-1&pivots=programming-language-python)

[Custom Vision Overview](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/overview)