import json

from django.test  import TestCase, Client
from product.models import CategoryProduct, ShopProduct

client = Client()

class JustTest(TestCase):
    def setUp(self):
        CategoryProduct.objects.create(
            id             = 1,
            image_url      = "'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/08/Downsizing_03-700x700.jpg'",
            tag            = "Feature",
            title          = "Downsizing",
            description    = "Unable to travel during lockdown, architects Salem Charabi & Rasmus Stroyberg decided to recreate a favorite building.",
            published_data = "None",
            category_id    = 1
        )
        ShopProduct.objects.create(
            id                      = 11,
            product_type            = "Books",
            outer_tag               = "The Kinfolk Garden",
            price                   = "40.00",
            outer_image_url         = "https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Thumb.jpg",
            inner_tag               = "The Kinfolk Garden ",
            inner_imgae_url         = "'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Cover_2048x683-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_10_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_17_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_20_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_46_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_62_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_67_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_73_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_75_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_82_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_84_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_115_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_117_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_127_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_136_2048x1365-1600x1066.jpg'",
            inner_description       = "Available for pre-order now\nFeaturing 30 inspiring people and places around the globe, The Kinfolk Garden offers an easy approach to bringing nature into your life. Following on from The Kinfolk Table, Home and Entrepreneur, the latest book from the team behind Kinfolk magazine focusses on beautiful spaces that bring the outdoors in and the indoors out. Divided into chapters on Care, Creativity and Community, the book explores the garden as a place for work, play, entertaining, and inspiration. Explore lush gardens and plant-filled homes, meet the inspiring people who coax them into bloom and learn from the experts about everything from arranging to eating plants and flowers.",
            inner_details           = "'368 pages, over 300 full colour photographs. Published by Artisan Books.', '–', 'Publication date: October 27, 2020'",
            inner_shipping_handling = "Kinfolk ships worldwide. Please proceed to the checkout to calculate the shipping price. Delivery times vary based on location as we ship from the USA and UK. For more information, please visit our FAQ page."
        )

    def test_DesignView_success(self):
        response = client.get('/categories/designs', content_type = 'application/json') 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {
                "Design": [
                    {
                        "id"             : 1,
                        "image_url"      : "'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/08/Downsizing_03-700x700.jpg'",
                        "tag"            : "Feature",
                        "title"          : "Downsizing",
                        "description"    : "Unable to travel during lockdown, architects Salem Charabi & Rasmus Stroyberg decided to recreate a favorite building.",
                        "published_data" : "None",
                        "category_id"    : 1
                    }
                ]
            }
        )
    
    def test_FashionView_success(self):
        response = client.get('/categories/fashions', content_type = 'application/json') 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {
                "Fashion": [
                    {
                        "id"             : 150,
                        "image_url"      : "'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/08/Rock_Steady_02-700x700.jpg'",
                        "tag"            : "Feature",
                        "title"          : "Rock Steady",
                        "description"    : "A breath of fresh air amid the ancient Stone Forest of southwestern China. ",
                        "published_data" : "None",
                        "category_id"    : 2
                    }
                ]
            }
        )

    def test_ShopView(self):
        response = client.get('/categories/shop', content_type = 'application/json') 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                "id"                      : 11,
                "product_type"            : "Books",
                "outer_tag"               : "The Kinfolk Garden",
                "price"                   : "40.00",
                "outer_image_url"         : "https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Thumb.jpg",
                "inner_tag"               : "The Kinfolk Garden ",
                "inner_imgae_url"         : "'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Cover_2048x683-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_10_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_17_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_20_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_46_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_62_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_67_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_73_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_75_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_82_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_84_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_115_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_117_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_127_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_136_2048x1365-1600x1066.jpg'",
                "inner_description"       : "Available for pre-order now\nFeaturing 30 inspiring people and places around the globe, The Kinfolk Garden offers an easy approach to bringing nature into your life. Following on from The Kinfolk Table, Home and Entrepreneur, the latest book from the team behind Kinfolk magazine focusses on beautiful spaces that bring the outdoors in and the indoors out. Divided into chapters on Care, Creativity and Community, the book explores the garden as a place for work, play, entertaining, and inspiration. Explore lush gardens and plant-filled homes, meet the inspiring people who coax them into bloom and learn from the experts about everything from arranging to eating plants and flowers.",
                "inner_details"           : "'368 pages, over 300 full colour photographs. Published by Artisan Books.', '–', 'Publication date: October 27, 2020'",
                "inner_shipping_handling" : "Kinfolk ships worldwide. Please proceed to the checkout to calculate the shipping price. Delivery times vary based on location as we ship from the USA and UK. For more information, please visit our FAQ page."
            }
        )
  
    def test_ShopBookView_success(self):
        response = client.get('/categories/shop/books', content_type = 'application/json') 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {
                "Books": [
                    {
                        "id"                      : 11,
                        "product_type"            : "Books",
                        "outer_tag"               : "The Kinfolk Garden",
                        "price"                   : "40.00",
                        "outer_image_url"         : "https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Thumb.jpg",
                        "inner_tag"               : "The Kinfolk Garden ",
                        "inner_imgae_url"         : "'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Cover_2048x683-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_10_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_17_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_20_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_46_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_62_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_67_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_73_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_75_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_82_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_84_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_115_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_117_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_127_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_136_2048x1365-1600x1066.jpg'",
                        "inner_description"       : "Available for pre-order now\nFeaturing 30 inspiring people and places around the globe, The Kinfolk Garden offers an easy approach to bringing nature into your life. Following on from The Kinfolk Table, Home and Entrepreneur, the latest book from the team behind Kinfolk magazine focusses on beautiful spaces that bring the outdoors in and the indoors out. Divided into chapters on Care, Creativity and Community, the book explores the garden as a place for work, play, entertaining, and inspiration. Explore lush gardens and plant-filled homes, meet the inspiring people who coax them into bloom and learn from the experts about everything from arranging to eating plants and flowers.",
                        "inner_details"           : "'368 pages, over 300 full colour photographs. Published by Artisan Books.', '–', 'Publication date: October 27, 2020'",
                        "inner_shipping_handling" : "Kinfolk ships worldwide. Please proceed to the checkout to calculate the shipping price. Delivery times vary based on location as we ship from the USA and UK. For more information, please visit our FAQ page."
                    }
                ]
            }

        )

    def test_ShopMagazineView_success(self):
        response = client.get('/categories/shop/magazines', content_type = 'application/json') 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {
                "Magazines": [
                    {
                        "id"                      : 17,
                        "product_type"            : "Magazine",
                        "outer_tag"               : "Issue 37",
                        "price"                   : "18.00",
                        "outer_image_url"         : "https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/K37_Product_Cover_Thumb-150x150.jpg",
                        "inner_tag"               : "Issue Thirty-Seven",
                        "inner_imgae_url"         : "'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/K37_Cover_Product_1024x683.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/K37_Product_2_1024x683.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/K37_Product_7_1024x683.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/K37_Product_3_1024x683.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/K37_Product_6_1024x683.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/K37_Product_4_1024x683.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/K37_Product_1_1024x683.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/K37_Product_8_1024x683.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/K37_Product_9_1024x683.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/01/K37_Product_5_1024x683.jpg'",
                        "inner_description"       : "The importance of nature for both our personal wellbeing and global prosperity has never been clearer. With a cautious return to the great outdoors now on our shared horizon, Kinfolk heeds the enticing call of the wild.",
                        "inner_details"           : "'192 pages, offset-printed and perfect bound, full color on uncoated and coated paper. Printed in the United Kingdom.', 'Publication date: September 8th, 2020'",
                        "inner_shipping_handling" : "Kinfolk ships worldwide. Please proceed to the checkout to calculate the shipping price. Delivery times vary based on location. For more information, please visit our FAQ page."
                    }
                ]

            }
        )

    def test_ProductDetail_success(self):
        response = client.get('/categories/shop/products?item=1', content_type = 'application/json') 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
        {
        "Detail": [
        {
            "id"                      : 1,
            "product_type"            : "Art Prints",
            "outer_tag"               : "How To Wear A Hat",
            "price"                   : "142.00",
            "outer_image_url"         : "https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/06/The_Kinfolk_Print_Collection_Product_thumb-1000x1000_001.jpg",
            "inner_tag"               : "How To Wear A Hat ",
            "inner_imgae_url"         : "'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/06/The_Kinfolk_Print_Collection_Product_1500x1000_001.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/06/The_Kinfolk_Print_Collection_Product_1500x1000_014.jpg'",
            "inner_description"       : "Simone Cavadini is a Swiss-Italian still life photographer based in Paris, and a former recipient of the Swiss Art Awards. For Kinfolk’s Summer 2018 issue, Cavadini was commissioned to compose still life images illustrating the editorial theme of the issue: Hair. The image featured in The Kinfolk Print Collection was part of a series exploring how hair holds deep and powerful meanings in daily life as a site of self-expression and a repository of cultural identity. Cavadini recognized the geometric quality in every-day brushes and combs, and transformed them into abstract compositions.",
            "inner_details"           : "'50 x 70 cm', 'High quality Giclée* print on 265g fine art paper', 'Open edition', '*Giclée is a fine art printing process combining long-lasting archival inks with high quality art paper achieving prints of high-quality and deep vibrant color.'",
            "inner_shipping_handling" : "All orders are shipped worldwide on our behalf by ALIUM, using DHL Express from Denmark. Shipping confirmation and tracking details will be sent by email. Please note that all prints will be shipped separately if ordering multiple items."
        }
    ]
}
        
        )
      
    def test_ProductDetail(self):
        response = client.get('/categories/shop/products?item=1', content_type = 'application/json') 
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), 
            {
                'MESSAGE': 'SUCCESS'
            }
        )
    def test_ProductDetail(self):
        response = client.get('/categories/shop/products?item=1', content_type = 'application/json') 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {
                'MESSAGE': 'SUCCESS'
            }
        )

    def test_SearchView_book_search_success(self):
        response = client.get('/search/book', content_type = 'application/json') 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                "search_results": [
                    [
                        {
                            "id"                      : 11,
                            "product_type"            : "Books",
                            "outer_tag"               : "The Kinfolk Garden",
                            "price"                   : "40.00",
                            "outer_image_url"         : "https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Thumb.jpg",
                            "inner_tag"               : "The Kinfolk Garden ",
                            "inner_imgae_url"         : "'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Cover_2048x683-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_10_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_17_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_20_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_46_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_62_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_67_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_73_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_75_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_82_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_84_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_115_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_117_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_127_2048x1365-1600x1066.jpg', 'https://24hkto1dz1v3ddyf93n0ye45-wpengine.netdna-ssl.com/wp-content/uploads/2020/04/TKG_Product_Spread_136_2048x1365-1600x1066.jpg'",
                            "inner_description"       : "Available for pre-order now\nFeaturing 30 inspiring people and places around the globe, The Kinfolk Garden offers an easy approach to bringing nature into your life. Following on from The Kinfolk Table, Home and Entrepreneur, the latest book from the team behind Kinfolk magazine focusses on beautiful spaces that bring the outdoors in and the indoors out. Divided into chapters on Care, Creativity and Community, the book explores the garden as a place for work, play, entertaining, and inspiration. Explore lush gardens and plant-filled homes, meet the inspiring people who coax them into bloom and learn from the experts about everything from arranging to eating plants and flowers.",
                            "inner_details"           : "'368 pages, over 300 full colour photographs. Published by Artisan Books.', '–', 'Publication date: October 27, 2020'",
                            "inner_shipping_handling" : "Kinfolk ships worldwide. Please proceed to the checkout to calculate the shipping price. Delivery times vary based on location as we ship from the USA and UK. For more information, please visit our FAQ page."
                        }
            
                    ]
                ]
            }
        
        )
      
    def test_SearchView_no_result(self):
        response = client.get('/search/dkdjkgugj', content_type = 'application/json') 
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), 
            {
                'Massage': 'No results found'
            }
        )
