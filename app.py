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
               "name": "Peacolate 18Months-12T Toddler Big Girls Pants Clothing Set 2pcs Cotton top and Jeans",
               "price": "$10 - $39",
               "image": "https://m.media-amazon.com/images/I/61VRnBvlxrL._AC_SX679_.jpg",
               "link": "https://amzn.to/4h3jYFt"
            },
            {
               "name": "Rihanna: and the Clothes She Wears Hardcover - April 18, 2023",
               "price": "$39.00",
               "image": "https://m.media-amazon.com/images/I/81C1-TzkcDL._SY385_.jpg",
               "link": "https://amzn.to/4hdv9ee"
            },
            {
               "name": "ACOCOPY Girls Gymnastics Leotards Sparkly Dance Unitards for Girls 4-11 Years",
               "price": "$29.88",
               "image": "https://m.media-amazon.com/images/I/91tgQRHU25L.__AC_SX300_SY300_QL70_ML2_.jpg",
               "link": "https://amzn.to/4hsKZBX"
            },
            {
               "name": "EVALESS Cropped Puffer Vest Women",
               "price": "$56.99",
               "image": "https://m.media-amazon.com/images/I/71u2GZ87poL._AC_SY606_.jpg",
               "link": "https://amzn.to/40unMKb"
            },
            {
               "name": "Zeagoo Flannels for Women",
               "price": "$36.99",
               "image": "https://m.media-amazon.com/images/I/811YeHAEWcL._AC_SX466_.jpg",
               "link": "https://amzn.to/4fR9aZB"
            },
            {
               "name": "OTEN Women's Two Piece Outfits Sweater Sets",
               "price": "$82.99",
               "image": "https://m.media-amazon.com/images/I/51SUqIzrXzL._AC_SY606_.jpg",
               "link": "https://amzn.to/4haz9vY"
            },
            {
               "name": "Basicspace Women's Scoop Neck Long Sleeve",
               "price": "$28.99",
               "image": "https://m.media-amazon.com/images/I/61BUFupVY7L._AC_SY606_.jpg",
               "link": "https://amzn.to/429wTRv"
            },
            {
               "name": "Taylor Swift Style: Fashion Through the Eras Hardcover",
               "price": "$27.99",
               "image": "https://m.media-amazon.com/images/I/71ixsuQYb+L._SY425_.jpg",
               "link": "https://amzn.to/4gOjpPK"
            },
            {
               "name": "JTAISC Women Crewneck Oversized Sweatshirt",
               "price": "$29.99",
               "image": "https://m.media-amazon.com/images/I/81evnRpjADL._AC_SY606_.jpg",
               "link": "https://amzn.to/4haz9vY"
            },
            {
               "name": "Sunzel Workout Leggings for Women",
               "price": "$23.99",
               "image": "https://m.media-amazon.com/images/I/61I7FpgX9IL._AC_SY606_.jpg",
               "link": "https://amzn.to/4jbzOPB"
            },
            {
               "name": "Fashion Angels Fashion Design Portfolio",
               "price": "$14.03",
               "image": "https://m.media-amazon.com/images/I/91tgQRHU25L.__AC_SX300_SY300_QL70_ML2_.jpg",
               "link": "https://amzn.to/40qTQP0"
            },
            {
               "name": "YEOREO Professional Women Workout Shorts",
               "price": "$23.99",
               "image": "https://m.media-amazon.com/images/I/61Pk5y2cgJL._AC_SX466_.jpg",
               "link": "https://amzn.to/4akG3Ni"
            },
            {
               "name": "YEOREO Scrunch Butt Workout Shorts Women",
               "price": "$29.99",
               "image": "https://m.media-amazon.com/images/I/812TPtYeuOL._AC_SX466_.jpg",
               "link": "https://amzn.to/40duTVF"
            },
            {
               "name": "BenSorts Women Men Pillow Sandals",
               "price": "$26.99",
               "image": "https://m.media-amazon.com/images/I/71eSyLKOd8L._AC_SX625_.jpg",
               "link": "https://amzn.to/4hdOegF"
            },
            {
               "name": "Boutique Fleece Belt Bag",
               "price": "$27.99",
               "image": "https://m.media-amazon.com/images/I/81Dlu8ZsY9L._AC_SX679_.jpg",
               "link": "https://amzn.to/4gOGHoF"
            },
            {
                "name": "FRIENDLY DIAMONDS Diamond Pendant Necklace For Women | 1 Carat - 3 Carat IGI Certified Lab Grown Diamond",
                "price": "$1,170.00",
                "image": "https://m.media-amazon.com/images/I/61aGa+rHWAL._AC_SX679_.jpg",
                "link": "https://amzn.to/4afexRl"
            },
            {
                "name": "Little Book of Dolce & Gabbana: The story of the iconic fashion house Hardcover - Nov. 7 2024",
                "price": "$22.99",
                "image": "https://m.media-amazon.com/images/I/619n9vdIg3L._SY425_.jpg",
                "link": "https://amzn.to/4aePr4X"
            },
            {
                "name": "vinnercoco High Top Sneakers for Women Canvas Shoes Fruits Embroidery High Tops Women Casual Shoes Lace Up Fashion Sneakers",
                "price": "$32.99",
                "image": "https://m.media-amazon.com/images/I/71mMjUAfntL._AC_SY625_.jpg",
                "link": "https://amzn.to/4gOaZaR"
            },
            {
                "name": "New Balance Mens 608 V5 Casual Comfort",
                "price": "$46.09",
                "image": "https://m.media-amazon.com/images/I/71vdp4uqBqL._AC_SX575_.jpg",
                "link": "https://amzn.to/40qr9BI"
            },
            {
                "name": "ZMBCYG Womens Shoes Running Walking Slip On Sport Sneakers Casual Work Tennis Gym Lightweight Comfortable Shoes",
                "price": "$33.99",
                "image": "https://m.media-amazon.com/images/I/61d1fzlJAcL._AC_SY625_.jpg",
                "link": "https://amzn.to/4fU99UA"
            }
        ],
        'Health & Beauty': [
            {
                "name": "SMART DK Purse Insert Organizer for dior book tote Large Bag Insert Premium Purse Felt Insert Multiple Pockets, Dark Gray, Small",
                "price": "$35.99",
                "image": "https://m.media-amazon.com/images/I/61aORirlcOL._AC_SX679_.jpg",
                "link": "https://amzn.to/4h0SUXk"
            },
            {
                "name": "5 Couleurs Eyeshadow Palette - 439 Copper by Christian Dior for Women - 0.24 oz Eye Shadow",
                "price": "$123.11",
                "image": "https://m.media-amazon.com/images/I/71DrNP-BASL._AC_SX425_.jpg",
                "link": "https://amzn.to/4hnq9DY"
            },
            {
                "name": "Sauvage Elixir by Christian Dior for Men - 3.4 oz Perfume Spray",
                "price": "$126.55",
                "image": "https://m.media-amazon.com/images/I/51cZJe31YFL._AC_SX425_.jpg",
                "link": "https://amzn.to/4hsuGVH"
            },
            {
                "name": "KARUIZI All in One Makeup Kit for Makeup storage bag 2X14",
                "price": "$39.98",
                "image": "https://m.media-amazon.com/images/I/71n6kWjp+xL._AC_SX679_.jpg",
                "link": "https://amzn.to/42qGoff"
            },
            {
                "name": "KARUIZI All in One Makeup Kit for Makeup storage bag 2X14",
                "price": "39.98",
                "video": "https://a.co/d/bUXlBLs",
                "link": "https://amzn.to/40wH2VY"
            },
            {
                "name": "Ri Ri by Rihanna Eau De Parfum Spray (Tester) 3.4 oz",
                "price": "$84.99",
                "image": "https://m.media-amazon.com/images/I/51dhj0dEQ7L._AC_SX679_.jpg",
                "link": "https://amzn.to/3WxvC33"
            },
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