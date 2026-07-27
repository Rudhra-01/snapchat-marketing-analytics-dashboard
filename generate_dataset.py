import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime

fake = Faker()

random.seed(42)
np.random.seed(42)

# ----------------------------
# CONFIGURATION
# ----------------------------

NUM_ROWS = 10000

campaign_names = [
    "Summer Sale",
    "Fashion Fiesta",
    "Tech Launch",
    "Back To School",
    "Gaming Festival",
    "Beauty Week",
    "Food Carnival",
    "Travel Escape",
    "Fitness Challenge",
    "Winter Deals",
    "Spring Collection",
    "Mega Discount",
    "Holiday Specials",
    "Flash Sale",
    "Luxury Collection",
    "Snap Rewards",
    "Student Offers",
    "Weekend Blast",
    "Festival Bonanza",
    "Premium Launch"
]

ad_types = [
    "Story",
    "Spotlight",
    "Discover"
]

devices = [
    "Android",
    "iPhone"
]

genders = [
    "Male",
    "Female"
]

age_groups = [
    "18-24",
    "25-34",
    "35-44",
    "45+"
]

countries = {
    "India": {
        "Tamil Nadu": ["Chennai","Coimbatore","Madurai"],
        "Karnataka": ["Bengaluru","Mysuru"],
        "Maharashtra": ["Mumbai","Pune"]
    },
    "USA": {
        "California": ["Los Angeles","San Diego"],
        "Texas": ["Dallas","Houston"]
    },
    "UK": {
        "England": ["London","Manchester"]
    },
    "Canada": {
        "Ontario": ["Toronto","Ottawa"]
    },
    "Australia": {
        "New South Wales": ["Sydney"]
    }
}

records = []

start_date = datetime(2025,1,1)
end_date = datetime(2025,12,31)

date_range = pd.date_range(start_date,end_date)

for i in range(NUM_ROWS):

    date = random.choice(date_range)

    country = random.choice(list(countries.keys()))
    state = random.choice(list(countries[country].keys()))
    city = random.choice(countries[country][state])

    campaign = random.choice(campaign_names)

    ad_type = random.choice(ad_types)

    device = random.choice(devices)

    gender = random.choice(genders)

    age = random.choice(age_groups)

    impressions = random.randint(10000,150000)

    reach = random.randint(
        int(impressions*0.60),
        int(impressions*0.95)
    )

    video_views = random.randint(
        int(reach*0.55),
        reach
    )

    swipe_ups = random.randint(
        int(video_views*0.05),
        int(video_views*0.18)
    )

    clicks = random.randint(
        int(swipe_ups*0.60),
        swipe_ups
    )

    conversions = random.randint(
        int(clicks*0.05),
        max(int(clicks*0.25),1)
    )

    spend = round(random.uniform(500,8000),2)

    revenue = round(
        spend * random.uniform(1.2,4.5),
        2
    )

    engagement_rate = round(
        (clicks/reach)*100,
        2
    )

    ctr = round(
        (clicks/impressions)*100,
        2
    )

    roi = round(
        ((revenue-spend)/spend)*100,
        2
    )

    watch_time = round(
        random.uniform(5,60),
        2
    )

    records.append([

        date,

        f"CMP{1000+i}",

        campaign,

        ad_type,

        country,

        state,

        city,

        device,

        gender,

        age,

        impressions,

        reach,

        video_views,

        swipe_ups,

        clicks,

        conversions,

        spend,

        revenue,

        engagement_rate,

        ctr,

        roi,

        watch_time

    ])

columns = [

    "Date",

    "Campaign_ID",

    "Campaign_Name",

    "Ad_Type",

    "Country",

    "State",

    "City",

    "Device",

    "Gender",

    "Age_Group",

    "Impressions",

    "Reach",

    "Video_Views",

    "Swipe_Ups",

    "Clicks",

    "Conversions",

    "Spend",

    "Revenue",

    "Engagement_Rate",

    "CTR",

    "ROI",

    "Watch_Time_sec"

]

df = pd.DataFrame(records, columns=columns)

df.to_csv("snapchat_marketing_dataset.csv", index=False)

print("="*60)
print("Dataset Created Successfully!")
print("="*60)
print(df.head())
print("\nRows:", len(df))
print("Columns:", len(df.columns))
print("\nFile Saved As: snapchat_marketing_dataset.csv")