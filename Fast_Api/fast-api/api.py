from fastapi import FastAPI
import random

app = FastAPI()
# its more preferable to name a variable name as app here when using FastAPI


side_hustles = [
    "Freelancing - Start offering your skills online ",
    "Blogging - Create content and earn through ads and sponsored posts",
    "Affiliate Marketing - Promote other people's products and earn a commission",
    "Online Courses - Create and sell online courses",
    "Dropshipping - Sell products online without holding inventory",
    "Print on Demand - Sell custom products online without holding inventory",
    "Stock Market - Invest and watch yor monet grow",
    "Crypto trading - Buy and Sell digital assets",
    "Youtube - Create videos and earn through ads and sponsored content",
    "App Development - Create and sell apps",
    "E-commerce - Start an online store",
    "Social Media Marketing - Offer social media marketing services",
    "Web Development - Offer web development services",
    "Graphic Design - Offer graphic design services",
    "Virtual Assistant - Offer virtual assistant services",
    "SEO - Offer SEO services"
]

money_quotes = [
    "Money is a terrible master but an excellent servant.",
    "Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver.",
    "The lack of money is the root of all evil.",
    "Money is like a sixth sense – and you can’t make use of the other five without it.",
    "If you dont find a way to make money while you sleep, you will work until you die.",
    "The way to get started is to quit talking and begin doing.",
    "Formal education will make you a living; self-education will make you a fortune.",
    "The more you learn, the more you earn.",
    "Donot save what is left after spending, but spend what is left after saving.",
    "The only difference between a rich person and poor person is how they use their time.",
    "The best investment you can make is in yourself."
]

@app.get("/side_hustles")
def get_side_hustles():
    """Returns a random side hustle idea"""
    return {"side_hustles": random.choice(side_hustles)}
# def get_side_hustles(apikey: str):
    """Returns a random side hustle idea"""
    # if apikey != "1234567890":
    #     return {"error": "Invalid API Key"}
    return {"side_hustles": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_side_hustles():
# def get_money_quotes(apikey: str):
    """Returns a random money quote"""
    # if apikey != "1234567890":
    #     return {"error": "Invalid API Key"}
    return {"money_quotes" : random.choice(money_quotes)}