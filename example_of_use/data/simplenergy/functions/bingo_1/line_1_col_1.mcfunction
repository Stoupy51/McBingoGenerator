
#> simplenergy:bingo_1/line_1_col_1
#
# @within			function tag "first_bingo/line_1/column_1.json"
# @executed			as & at the player who completed the advancement
#
# @input macro		$(title)		"Title of the advancement"
# @input macro		$(description)	"Description of the advancement"
#
# @description		Executed when the player completes the advancement
#

$tellraw @a [{"text":"Le joueur "},{"selector":"@s"},{"text":" vient de compléter l'objectif ligne 1 colonne 1 "},{"text":"[$(title)]","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"$(description)","color":"gray"}}}]
scoreboard players add @s simplenergy.bingo_1 1

