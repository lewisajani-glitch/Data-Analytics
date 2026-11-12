import math

room_length = float(input("What is the room length in feet? "))
room_width = float(input("What is the room width in feet? "))
room_area = room_length * room_width

tiles_for_room = math.ceil(room_area)
tiles_with_extra = math.ceil(tiles_for_room * 1.10)

boxes_to_buy = math.ceil(tiles_with_extra / 12)
total_tiles_purchased = boxes_to_buy * 12

print(f"The room area is {room_area:.2f} square feet.")
print(f"Tiles needed for the room: {tiles_for_room}")
print(f"Tiles needed with at least 10% extra: {tiles_with_extra}")
print(f"You need to buy {boxes_to_buy} boxes ({total_tiles_purchased} tiles total).")