import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse or text_to_analyse.strip() == "":  # Check for blank input
        return {
            'status_code': 400,
            'dominant_emotion': None,
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
        }

    try:
        # URL of the emotion analysis service
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        
        # Create a dictionary with the text to be analyzed
        myobj = { "raw_document": { "text": text_to_analyse } }

        # Set the headers required for the API request
        header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

        # Send a POST request to the API with the text and headers
        response = requests.post(url, json=myobj, headers=header)

        # Parsing the json
        formatted_response = response.json ()

        # Access the dictionary
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']

        # Extracting the variables and values
        anger_score = emotion_data['anger']
        disgust_score = emotion_data['disgust']
        fear_score = emotion_data['fear']
        joy_score = emotion_data['joy']
        sadness_score = emotion_data['sadness']

        # Determine the dominant emotion
        dominant_emotion = max(emotion_data, key=emotion_data.get)

        # Return the response text from the json
        return {'anger': anger_score, 
                    'disgust': disgust_score, 
                    'fear': fear_score, 
                    'joy': joy_score, 
                    'sadness': sadness_score, 
                    'dominant_emotion': dominant_emotion}

    except Exception as e: #Catch any other exception
        print(f"Error in emotion_detector: {e}")
        return {
            'status_code': 500,  # Internal Server Error
            'dominant_emotion': None,
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'error_message': "An unexpected error occurred"
        }