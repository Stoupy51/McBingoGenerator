
## Python program that generates multiple random advancements and put them in the "generated_advancements" folder
import random
import requests
import json
import os

# Stop program if not executed from the root folder
if not os.path.exists("advancements_generator.py"):
	print("Please execute this program from its folder.")
	exit()

# Configuration
generation_folder = "generated_advancements"
number_of_advancements_to_generate = 1000
template = """{
	"display": {
		"icon": {
			"item": "___ITEM_ID___"
		},
		"title": {
			"text": "___ITEM_NAME___",
			"color": "aqua"
		},
		"description": {
			"text": "Obtenir un(e) ___ITEM_NAME___",
			"color": "gray"
		},
		"frame": "task",
		"show_toast": false,
		"announce_to_chat": false,
		"hidden": false
	},
	"criteria": {
		"requirement": {
			"trigger": "minecraft:inventory_changed",
			"conditions": {
				"items": [
					{
						"items": [
							"___ITEM_ID___"
						]
					}
				]
			}
		}
	},
	"requirements": [
		[
			"requirement"
		]
	]
}
"""


# Download a list of blocks
link = "https://raw.githubusercontent.com/PixiGeko/Minecraft-generated-data/master/1.20/releases/1.20.2/custom-generated/tags/all_blocks_with_drop.json"
temporary_file = "all_blocks_with_drop.json"
r = requests.get(link)
with open(temporary_file, "wb") as file:
	file.write(r.content)
blocks = dict(json.load(open(temporary_file, "r")))
os.remove(temporary_file)
blocks = blocks["values"]
if len(blocks) < number_of_advancements_to_generate:
	number_of_advancements_to_generate = len(blocks)


# Create the folder "generated_advancements" if it doesn't exist
if not os.path.exists(generation_folder):
	os.mkdir(generation_folder)

# Generate the advancements
for i in range(number_of_advancements_to_generate):

	# Choose a random block
	j = random.randint(0, len(blocks) - 1)
	block_id = blocks[j]
	blocks.pop(j)
	block_name = block_id.replace("minecraft:", "").replace("_", " ").title()
	print(f"Generating advancement for {block_name}...")
	
	# Create the advancement
	advancement = template.replace("___ITEM_ID___", block_id).replace("___ITEM_NAME___", block_name)
	
	# Save the advancement
	block_id = block_id.replace("minecraft:", "")
	with open(f"{generation_folder}/{block_id}.json", "w") as file:
		file.write(advancement)


