def predict_text(text):
    text = text.lower()
    if "yellow" in text or "மஞ்சள்" in text:
        return "Leaf Blight", 0.8
    elif "white powder" in text or "பூஞ்சை" in text:
        return "Powdery Mildew", 0.75
    elif "spots" in text:
        return "Fungal Infection", 0.7
    else:
        return "Healthy", 0.6
