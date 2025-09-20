import os
from tornado.template import Template
import tornado.escape

def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def write_file(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)

def generate_html_from_template(template_path, output_path, context):
    template_content = read_file(template_path)
    template = Template(template_content, autoescape=None)  # Disable autoescaping
    rendered_content = tornado.escape.xhtml_unescape(template.generate(**context))
    write_file(output_path, rendered_content)

def main():
    template_filepath = 'index_template.html'

    christmas_context = {
        "title": "Christmas Bingo!",
        "background_image_url": "./holly.jpeg",
        "color_scheme":  ['#ff0000', '#00a000', '#0000ff', '#ffbf00', '#9932CC'],
        "icon_emoji": "🎄",
        "marked_color": "#00a000",  # Or any color you want
        "board_emojis": "🎄🎅❄️⛄🎁",
        "tropes_list": [
                "City Slicker Finds Small-Town Love",
                "Attractive Widower or Devorcee",
                "Family Business Needs Saving",
                "Perfect Holiday Festival",
                "Workaholic Learns Holiday Spirit",
                "Small-Town Charm Wins Over Cynic",
                "Over-achiever Learns to Relax",
                "Small Town with Big Traditions",
                "Snowed-In!",
                "Sassy Friend Loves Holidays",
                "Snow Globe",
                
                "Grumpy Boss Finds Holiday Joy",
                
                "Miracle Saves the Holidays",
                "Special Ornament",
                "Big Family Gathering",
                "Adorable animal in a Santa Hat",
                "Romantic Carriage Ride in Town",
                "Epic Holiday Decor Showdown",
                
                "Snowfall at the Perfect Moment",
                "Mistletoe Kiss",
                "Holiday Schedule Chaos",
                "Big Secret Unveiled",
                
                "Hometown Hero Restores Spirit",
                "City Slicker Meets Rustic Charm",
                "Volunteer Event",
        
                "Clumsy Yet Sweet Helper",
                
                "Rivalry Over Decorations",
                "Magic Kiss on Christmas Eve",
                
                "Tree Lighting Ceremony",
                "Last-Minute Dash for Holiday Cheer",
                "Enemies Fall in Love at Christmas",
                "Town Legend of Christmas Magic",
                "Holiday Market",
                "Family Heirloom",
                "Assistant Finally Gets Their Moment",
                "Christmas Engagement",
                "Small-Town Love Interest",
                "City person can’t do small town things",
                "Secret Santa Gift with Meaning",
                "Plans Fall Apart",
                "Lost Pet Found",
                "Fake Dating Leads to Real Love",
                
                "Holiday Photoshoot",
                "Small-Town Festival",
                "Surprise Family Visit",
                "Holiday Costume Disaster",
                "Petty Argument Ends in Love",
                "Child Helps Adults Believe Again",
                "Snowball Fight",
                "Tree Farm",
                "Reindeer",
                "Hidden Talent",
                "Holiday Concert",
                "Holiday Grump",
                "Santa Stand-In",
                "Holiday Workaholic",
                "Over-bearing Relative",
                "Perfect Love Interest",
                "City Slicker",
                
                "Cynical Teen",
                "Grumpy Boss",
                "Elder shares wisdom",
                "Small Town with Big Christmas Spirit",
                "Family Cabin",
                "Busy Department Store",
                
                "Cozy Bakery",
                
                
                "Snowy Landscape",
                "Over-the-Top Holiday House",
                "Big City at Christmas",
                "'Save Christmas' Mission",
                "Mistaken Identity",
                "Holiday Bet or Dare",
                "Christmas Competition",
                "Return Home for the Holidays",
                "Christmas Wish",
                "Holiday Makeover",
                "Romantic Mix-Up",
                
                "Last-Minute Gift Dash",
                
                "Holiday Proposal",
                "Dcovery of True Meaning of Christmas",
                "Redemption and Forgiveness",
                "Overcoming Holiday Cynicism",
                "Conflict Across Generations",
                "Spirit of Giving",
                "Snowy Nights",
                "Mistletoe",
                "Caroling",
                
                "Ugly Christmas Sweaters",
                "Festive Food Feasts",
                "Christmas Markets",
                "Special Ornament",
                "Naughty or Nice",
                "Snow Globe",
                "Over-the-Top Neighbors",
                "Magical Creatures",
                "Stockings",
                "Christmas Lights",
                "Candy Canes",
                "Poinsettias",
                "Nativity Scenes",
                "Santa Claus",
                "Sitting with Santa",
                "Reindeer",
                "Sleighs",
                "Snowmen",
                
                "Gingerbread Houses",
                "Hot Cocoa or Eggnog",
                "Christmas Cookies",
                "Yule Log (Cake) or Fruit Cake",
                "Fire Roaring in the Fireplace",
                "Gift Wrapping Paper",
                "Christmas Morning",
                "Christmas Hits",
                "Holiday Movie Reference",
                "Christmas Villages",
                "Snowflakes",
                "Christmas Bells",
                "Santa Hats",
                "Winter Scarves",
                "Holiday Pajamas",
                "North Pole",
                "Christmas Elves",
                "Christmas Parties",
                "Gift Exchanges",
                "Caroling",
                
                "Snowball Fights",
                
                "Holiday Mugs",
                "Nutcracker",
                "French Horn in Soundtrack",
                "Sleigh Bells Ringing",
                "Christmas Stockings",
                "Festive Table Settings",
                "Holiday Baking",
                "Festive Wreaths",
                "Ice Skating",
                "Holiday Classics Music",
                "Holiday Magic",
                "Generous application of fake snow",
                "Generous application of hairspray",
            ],
        
    }
    
    generate_html_from_template(template_filepath, 'christmas.html', christmas_context)

    halloween_context = {
        "title": "Halloween Bingo!",
        "background_image_url": "./spooky.png",
        "color_scheme":  ['#9A4DFF', '#FFB347',  '#9A4DFF', '#FFB347', '#9A4DFF'],
        "icon_emoji": "🎃",
        "marked_color": "#FFB347",  # Or any color you want
        "board_emojis": "🎃👻🍬🕷️🦇",
        "tropes_list": [
            "Jump Scare False Alarm",
            "Flashlight Batteries Die",
            "‘Let’s Split Up!’",
            "Mirror Scare",
            "Phone With No Signal",
            "Final Girl Energy",
            "Creepy Basement",
            "Chainsaw Guy",
            "Haunted Objects",
            "Eerie Lullabies",
            "Candy",
            "I'm Not Afraid!",
            "Stormy Night",
            "Car Won’t Start",
            "Running Upstairs Instead of Out",
            "Look Behind You",
            "Killer appears in Background",
            "The Killer Moves Really Slowly…",
            "Random Cat Jumping Out",
            "Stranger Knows Too Much",
            "‘It Was Just a Dream’",
            "Evil Laugh",
            "Possessed Child",
            "Old TV Static",
            "Locked From the Outside",
            "Flickering Lights",
            "The Call Is Coming From Inside the House",
            "Ancient Cursed Object",
            "Pumpkin Patch",
            "Local Legend",
            "Abrupt Weather Change",
            "Endless Fog Machine",
            "Fake-Out Death",
            "Evil Script",
            "Crowd Gasps in Unison",
            "Killer’s Mask Reveal",
            "Magic Book Nobody Should Open",
            "Make fun of Horror Clichés",
            "Blood on the Mirror",
            "Jump Cut to Screaming",
            "Safe then Not Safe",
            "Costumes",
            "Trick or Treating",
            "Haunted House Attraction",
            "Pumpkin Carving",
            "Spooky Decorations",
            "Full Moon",
            "Creepy Doll",
            "Monsters",
            "Killer is friend or family",
            "Killer is among us",
            "Killer theme music",
            "Good turned bad",
        ]

    }
    generate_html_from_template(template_filepath, 'halloween.html', halloween_context)

if __name__ == "__main__":
    main()
