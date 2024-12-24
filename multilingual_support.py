import translate

    def get_preferred_language(lead_info):
        # Get the preferred language from the lead information
        preferred_language = lead_info["preferred_language"]
        return preferred_language

    def translate_message(message, language):
        # Translate the message to the preferred language
        translated_message = translate.translate(message, dest=language).text
        return translated_message
