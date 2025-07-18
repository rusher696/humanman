food_db = {
    "banana": {
        "calories": 89,
        "carbs": 23,
        "proteins": 1.1,
        "fats": 0.3,
        "digest_time_hr": 2
    },
    "egg": {
        "calories": 78,
        "carbs": 0.6,
        "proteins": 6,
        "fats": 5,
        "digest_time_hr": 3
    },
    "apple": {
        "calories": 52,
        "carbs": 14,
        "proteins": 0.3,
        "fats": 0.2,
        "digest_time_hr": 1.5
    }
}
class digest:
    def eat(food):
        """
        Tells digestion stats if in database.
        """
        food = food.lower().strip()
        if not food in food_db:
            return {
            "food": None,
            "calories": None,
            "carbs": None,
            "proteins": None,
            "fats": None,
            "digest_time_hr": None,
            "atp": None,
            "error": f"Unknown food: {food} (use addFood() to use!)"
            }
        f = food_db[food]
        try:
            atp = (f["calories"] * 4184) / 30
            return {
            "food": food,
            "calories": f.get("calories"),
            "carbs": f.get("carbs"),
            "proteins": f.get("proteins"),
            "fats": f.get("fats"),
            "digest_time_hr": f.get("digest_time_hr"),
            "atp": atp,
            "error": None
            }
        except Exception as e:
            return {
            "food": None,
            "calories": None,
            "carbs": None,
            "proteins": None,
            "fats": None,
            "digest_time_hr": None,
            "atp": None,
            "error": str(e)
            }
    def addFood(name, calories, carbs, proteins, fats, digest_time_hr):
        """
        Adds a food to the food database.
        Input: name, calories, carbs, proteins, fats, digest time in hours
        Output: success, status, error, added to database
        """
        try:
            fooddict = {
            "calories": int(calories),
            "carbs": int(carbs),
            "proteins": int(proteins),
            "fats": int(fats),
            "digest_time_hr": int(digest_time_hr)
            }
            food_db[name.lower().strip()] = fooddict
            return {
            "success": True,
            "status": f"Added {name} to the food database with contents {fooddict}.",
            "error": None
            }
        except Exception as e:
            return {
            "success": False,
            "status": f"Failed adding {name} to the food database.",
            "error": str(e)
            }             