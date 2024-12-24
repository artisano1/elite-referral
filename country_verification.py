def verify_country(lead_info):
        # Verify the country of the lead
        country = lead_info["country"]
        if country in ["USA", "Canada", "Mexico"]:
            return True
        else:
            return False
