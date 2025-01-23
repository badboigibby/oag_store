from flask import Flask, render_template

app = Flask(__name__)  # Initialize the Flask app

import sys
sys.path.append('/home/badoigibbiy/oag_store')  # Your actual project path

# Import your Flask app from the correct file (app.py)
from app import app as application




# Product data categorized by sections
products = {
        'Fashion': [
            {
                "name": "LANEIGE Lip Sleeping Mask: Nourish, Hydrate, Vitamin C, Murumuru & Shea Butter, Antioxidants, Flaky, Dry Lips",
                "price": "$32.50",
                "link": "https://amzn.to/3WheZZg",
                "image": "https://m.media-amazon.com/images/I/71vornnrsqL._SX522_.jpg"
            },
            {
                "name": "LANEIGE Lip Sleeping Mask: Nourish, Hydrate, Vitamin C, Murumuru & Shea Butter, Antioxidants, Flaky, Dry Lips",
                "price": "32.50$",
                "link": "https://amzn.to/4aerjzg",
                "image": "https://m.media-amazon.com/images/I/81WkKgs0TXL._SX522_.jpg"
            },
            {
                "name": "Wet n Wild Always Naked Palette Always Nude",
                "price": "5.79$",
                "link": "https://amzn.to/3PAjVox",
                "image": "https://m.media-amazon.com/images/I/71-ekZvH8qL._AC_SX425_.jpg"
            },
            {
                "name": "Dove Exfoliating Body Polish moderate exfoliant Macadamia & Rice Milk gentle to skin microbiome 298 g",
                "price": "13.49$",
                "link": "https://amzn.to/4h972xf",
                "image": "https://m.media-amazon.com/images/I/71LCd79G2bL._AC_SX425_.jpg"
            },
            {
                "name": "Fenty Beauty by Rihanna Match Stix Corrector Skinstick Rose Quartz",
                "price": "34.44$",
                "link": "https://amzn.to/3DUEUzN",
                "image": "https://m.media-amazon.com/images/I/41n-jUuQTNL._AC_SX679_.jpg"
            },
            {
                "name": "FENTY BEAUTY BY RIHANNA Killawatt Freestyle Highlighter Color: Lightning Dust/Fire Crystal",
                "price": "59.99",
                "link": "https://amzn.to/40jW4hY",
                "image": "https://m.media-amazon.com/images/I/51UQUa3VZ3L._AC_SX679_.jpg"
            },
            {
                "name": "Fenty Beauty by Rihanna Body Sauce Body Luminizing Tint 02 Hunnie Hunnie",
                "price": "57.00$",
                "link": "https://amzn.to/42bOR5P",
                "image": "https://m.media-amazon.com/images/I/41zlCnVLXmL._AC_SX679_.jpg"
            },
            {
                "name": "Fenty Beauty by Rihanna Pro Filt'r Soft Matte Longwear Foundation - 450",
                "price": "85.00$",
                "link": "https://amzn.to/3PuAFxt",
                "image": "https://m.media-amazon.com/images/I/41wyEBwi5uL._AC_SX679_.jpg"
            },
            {
                "name": "Rihanna Rough Love By Eau De Parfum, 4.2 ounces",
                "price": "61.99$",
                "link": "https://amzn.to/3DO3m5I",
                "image": "https://m.media-amazon.com/images/I/71aiDgwTiKL._AC_SX679_.jpg"
            },
            {
                "name": "Glamnetic Press On Nails - Red Affair",
                "price": "$26.99",
                "image": "https://m.media-amazon.com/images/I/71PMs97X-AL._AC_SX425_.jpg",
                "link": "https://amzn.to/3WgDaHg"
            
            },
            {
                "name": "LIBRE LE PARFUM YVES SAINT LAURENT by Yves Saint Laurent, EAU DE PARFUM SPRAY 1 OZ",
                "price": "$154.95",
                "image": "https://m.media-amazon.com/images/I/51iTqDarPAL._AC_SY879_.jpg",
                "link": "https://amzn.to/3DKbhB1"
            },
            {
                "name": "e.l.f. SKIN Bronzing Drops, Liquid Bronzer For Face & Skin, Creates A Sun-Kissed Glow, Infused With Vitamin E, Vegan & Cruelty-Free, Pure Gold",
                "price": "$16.00",
                "image": "https://m.media-amazon.com/images/I/714oMG76kAL._AC_SX425_.jpg",
                "link": "https://amzn.to/4fSmn4q"
            },
            {
                "name": "L Oréal Paris True Match Lumi Glotion, Natural Glow Enhancer, Illuminating Tinted Moisturizer and Lotion for Face and Body, Shade: Deep, 1.35 fl. Oz",
                "price": "$15.58",
                "image": "https://m.media-amazon.com/images/I/61oqxz0k9bL._AC_SX425_.jpg",
                "link": "https://amzn.to/4gR8Rzc"
            },
            {
                "name": "e.l.f. SKIN Bronzing Drops, Liquid Bronzer For Face & Skin, Creates A Sun-Kissed Glow, Infused With Vitamin E, Vegan & Cruelty-Free, Pure Gold",
                "price": "$16.00",
                "image": "https://m.media-amazon.com/images/I/91U7O2prDmL._AC_SX425_.jpg",
                "link": "https://amzn.to/3C53I7y"
            },
            {
                "name": "e.l.f. SKIN Bronzing Drops, Liquid Bronzer For Face & Skin, Creates A Sun-Kissed Glow, Infused With Vitamin E, Vegan & Cruelty-Free, Pure Gold",
                "price": "$16.00",
                "image": "https://m.media-amazon.com/images/I/81TuAmhMkSL._AC_SX425_.jpg",
                "link": "https://amzn.to/4heoyk1"
            },
            {
                "name": "e.l.f. Glow Reviver Lip Oil, Nourishing Tinted Lip Oil For A High-shine Finish, Infused With Jojoba Oil, Vegan & Cruelty-free, Rose Envy",
                "price": "$9.48",
                "image": "https://m.media-amazon.com/images/I/616YIg55gvL._AC_SX425_.jpg",
                "link": "https://amzn.to/40tl1Zi"
            },
            {
                "name": "e.l.f. Glow Reviver Lip Oil, Nourishing Tinted Lip Oil For A High-shine Finish, Infused With Jojoba Oil, Vegan & Cruelty-free, Rose Envy",
                "price": "$9.48",
                "image": "https://m.media-amazon.com/images/I/71st0rWsKGL._AC_SX425_.jpg",
                "link": "https://amzn.to/40tl9rK"
            },
            {
                "name": "BEAKEY Makeup Brushes Set, Professional Foundation Eyeshadow Concealer Blush Powder Bronzer Applicator, 2 Blender Sponge wit Beauty Paper Case, Gifts for Women Christmas Stocking Stuffers for Adults",
                "price": "$14.99",
                "image": "https://m.media-amazon.com/images/I/717GzR2ODrL._AC_SX425_.jpg",
                "link": "https://amzn.to/3DSHx5d"
            }
            # Add more beauty & health items here...
        ],
        'Sports & Games': [
            {
                "name": "Holure Men's Sports Running Set",
                "price": "$46.99",
                "image": "https://m.media-amazon.com/images/I/61P+6gDSrML._AC_SX679_.jpg",
                "link": "https://amzn.to/42b81ZJ"
            },
            {
                "name": "Runhit Long Sleeve Compression Shirts for Men",
                "price": "$31.99",
                "image": "https://m.media-amazon.com/images/I/61rHqv6uz1L._AC_SX679_.jpg",
                "link": "https://amzn.to/4gOhta1"
            
            },
            {
                "name": "PUMA mens Puma Evercat Contender 3.0 Duffel Duffel Bags",
                "price": "$41.85",
                "image": "https://m.media-amazon.com/images/I/91uNUOF8gfL._AC_SX679_.jpg",
                "link": "https://amzn.to/4jeUztO"
            },
            {
                "name": "Basketball Hoop for Kids, Mini Indoor Basketball Hoop with 4 Balls Indoor Basketball Toys for 6 7 8 9 10 11 12 13 14 Year Old Sport Toys Birthday Gift",
                "price": "$51.99",
                "image": "https://m.media-amazon.com/images/I/91KbLtxYIFL._AC_SX679_.jpg",
                "link": "https://amzn.to/4affNno"
            },
            {
                "name": "Sports Balls for Kids and Toddlers (Pack of 4) with Hand Pump 6-inch Diameter Rubber Sport Ball Kids Outdoor Toys & Toddlers. Mini Football Mini Basketball Kids Soccer Ball & Playground Ball",
                "price": "$19.99",
                "image": "https://m.media-amazon.com/images/I/91NECTHr3iL._AC_SX425_.jpg",
                "link": "https://amzn.to/42a9Ypb"
            },
            {
                "name": "Jacked Factory Creatine Monohydrate Powder 425g - Creatine Supplement for Increased Muscle Mass*, Improved Strength, Power, & Performance** - 85 Servings, Unflavored",
                "price": "$23.99",
                "image": "https://m.media-amazon.com/images/I/61w-LchQ3xL._AC_SY679_.jpg",
                "link": "https://amzn.to/40aud3E"
            },
            {
                "name": "Zacro Resistance Bands Set - Pull Up Bands Set for Men and Women - Exercise Loop Bands with Door Anchor, Training Poster & Pouch for Workout Home Gym Exercise, Yoga, Pull Up Assistance Bands",
                "price": "$39.99",
                "image": "https://m.media-amazon.com/images/I/71p6dAKPG9L._AC_SX425_.jpg",
                "link": "https://amzn.to/4hdBtlV"
            },
            {
                "name": "Ajmori 1200LB Weight Bench,Workout Bench For Home Gym,Multi-Angle Adjustable Strength Training Benchs for Full Body Workout",
                "price": "$132.99",
                "image": "https://m.media-amazon.com/images/I/71TXp2PJprL._AC_SX679_.jpg",
                "link": "https://amzn.to/4gVGpfF"
            },
            {
                "name": "Resistance Bands, Exercise Bands, Physical Therapy Bands for Strength Training, Yoga, Pilates, Stretching, Stretch Elastic Band with Different Strengths, Workout Bands for Home Gym",
                "price": "$14.96",
                "image": "https://m.media-amazon.com/images/I/61QR7buI+FL._AC_SX425_.jpg",
                "link": "https://amzn.to/4fNTLt2"
            }
            # Add more sports & games items here...
        ],
        'Electronics': [
            {
                "name": "Wireless Earbuds",
                "price": "$29.00",
                "image": "https://m.media-amazon.com/images/I/81H9uMsZ7gL._AC_SX425_.jpg",
                "link": "https://amzn.to/3C2GuPv"
            },
            {
                "name": "Heavy Duty iPhone 11 Case",
                "price": "$15.19",
                "image": "https://m.media-amazon.com/images/I/81TLZlfifLL._AC_SX679_.jpg",
                "link": "https://amzn.to/3DPNBeI"
            },
            {
                "name": "Deeyaple Portable Bluetooth Speaker",
                "price": "$29.99",
                "image": "https://m.media-amazon.com/images/I/81nVPBGFZvL._AC_SX679_.jpg",
                "link": "https://amzn.to/40eQ0qK"
            },
            {
                "name": "Smart Watch for Men Women with Bluetooth",
                "price": "$39.99",
                "image": "https://m.media-amazon.com/images/I/710b8fmU7wL._AC_SX425_.jpg",
                "link": "https://amzn.to/40qiSxw"
            },
            {
                "name": "Amazon Fire HD 10 Tablet",
                "price": "$299.99",
                "image": "https://m.media-amazon.com/images/I/51-6uBmjPqL._AC_SY450_.jpg",
                "link": "https://amzn.to/4jab76a"
            },
            {
                "name": "KTC 27 Inch QHD (2560 x 1440) Monitor",
                "price": "$159.99",
                "image": "https://m.media-amazon.com/images/I/71jJvJ5noCL._AC_SX425_.jpg",
                "link": "https://amzn.to/3C4Xapt"
            },
            {
                "name": "Google Pixel 9-128 GB - Unlocked Android Smartphone with Advanced Pixel Camera",
                "price": "$1099.00",
                "link": "https://amzn.to/4h7h0PR",
                "image": "https://m.media-amazon.com/images/I/51Qa+x-KUWL._AC_SX679_.jpg"
            },
            {
                "name": "Google Pixel 9 Pro - 128 GB - 6.3-inch Display - Unlocked Android Smartphone",
                "price": "$1349.99",
                "link": "https://amzn.to/42a7jvH",
                "image": "https://m.media-amazon.com/images/I/31FQZRRqlRL._AC_SX679_.jpg"
            },
            {
                "name": "Google Pixel 9 Pro Fold - Unlocked Android Smartphone with Gemini",
                "price": "$2399.99",
                "link": "https://amzn.to/40qCPV4",
                "image": "https://m.media-amazon.com/images/I/61obpR7xQ+L._AC_SX679_.jpg"
            },


            # Add more electronics items here...
        ]
    }

@app.route('/')
def home():
    # Pass categories and products to the template
    return render_template('index.html', categories=products.keys(), products=products)