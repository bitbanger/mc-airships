LNW = (-8564, 131, -1986)
USE = (-8550, 141, -1972)

PORT = (-8564, 65, -2028)
REVERSE = (-8560, 65, -2025)
STARBOARD = (-8557, 65, -2029)
UP = (-8557, 65, -2025)
DOWN = (-8564, 65, -2025)
FORWARD = (-8561, 65, -2032)
NETHER = (-8560, 134, -1973)
OVERWORLD = (-8563, 134, -1975)

SHIP_NAME = 'obelisk'

def to_lnw(blk):
	return (LNW[0]-blk[0], LNW[1]-blk[1], LNW[2]-blk[2])

def to_use(blk):
	return (USE[0]-blk[0], USE[1]-blk[1], USE[2]-blk[2])

def delta(n):
	if n == 0:
		return '~'
	else:
		return '~%d' % (n)



def mk_cmds(dr, dr_dest_nums, pillar_facing, ship_name, dimension=None):
	drive2_mod = [0, 0, 0]
	if pillar_facing == 'up':
		drive2_mod[1] -= 1
	elif pillar_facing == 'down':
		drive2_mod[1] += 1
	elif pillar_facing == 'north':
		drive2_mod[2] += 1
	elif pillar_facing == 'south':
		drive2_mod[2] -= 1
	elif pillar_facing == 'east':
		drive2_mod[0] -= 1
	elif pillar_facing == 'west':
		drive2_mod[0] += 1

	dr_drive1_nums = tuple([USE[0]-dr[0], (USE[1]-dr[1])+2, USE[2]-dr[2]])
	dr_drive2_nums = tuple([(USE[0]-dr[0])+drive2_mod[0], (USE[1]-dr[1])+2+drive2_mod[1], (USE[2]-dr[2])+1+drive2_mod[2]])
	dr_drive_facing = 'south'

	drive1 = (dr[0] + dr_drive1_nums[0], dr[1] + dr_drive1_nums[1], dr[2] + dr_drive1_nums[2])
	dr_lnw_delt = [delta(x) for x in to_lnw(drive1)]
	dr_use_delt = [delta(x) for x in to_use(drive1)]
	dr_dest_delt = [delta(to_lnw(drive1)[i] + dr_dest_nums[i]) for i in range(len(dr_dest_nums))]
	if dimension:
		print '/setblock %s %s %s minecraft:command_block[facing=%s]{%sCommand:"/execute in minecraft:%s clone %s %s %s %s %s %s %s %s %s replace move"}' % tuple([delta(dr_drive1_nums[0]), delta(dr_drive1_nums[1]), delta(dr_drive1_nums[2]), dr_drive_facing, 'auto:1,' if True else '', dimension] + dr_lnw_delt + dr_use_delt + dr_dest_delt)
	else:
		print '/setblock %s %s %s minecraft:command_block[facing=%s]{%sCommand:"/clone %s %s %s %s %s %s %s %s %s replace move"}' % tuple([delta(dr_drive1_nums[0]), delta(dr_drive1_nums[1]), delta(dr_drive1_nums[2]), dr_drive_facing, 'auto:1,' if True else ''] + dr_lnw_delt + dr_use_delt + dr_dest_delt)
	
	drive1_from_drive2 = [0, 0, 0]
	if dr_drive_facing == 'north':
		drive1_from_drive2[2] += 1
	elif dr_drive_facing == 'south':
		drive1_from_drive2[2] -= 1
	elif dr_drive_facing == 'east':
		drive1_from_drive2[0] -= 1
	elif dr_drive_facing == 'west':
		drive1_from_drive2[0] += 1
	
	print '/setblock %s %s %s minecraft:chain_command_block[facing=%s]{auto:1,Command:"/fill %s %s %s ~ ~ ~ minecraft:air"}' % tuple([delta(dr_drive2_nums[0]), delta(dr_drive2_nums[1]), delta(dr_drive2_nums[2]), dr_drive_facing, delta(drive1_from_drive2[0]), delta(drive1_from_drive2[1]), delta(drive1_from_drive2[2])])


	x_tp = 0
	y_tp = 0
	z_tp = 0
	if dr == UP:
		y_tp += 1.5 * dr_dest_nums[1]
	elif dr == DOWN:
		y_tp -= 0.5 * dr_dest_nums[1]
	elif dr == PORT:
		x_tp -= 1 * dr_dest_nums[0]
	elif dr == STARBOARD:
		x_tp += 1 * dr_dest_nums[0]
	elif dr == FORWARD:
		z_tp -= 1 * dr_dest_nums[2]
	elif dr == REVERSE:
		z_tp += 1 * dr_dest_nums[2]

	if dimension:
		print '/execute in minecraft:%s as @a[tag=%s] at @s run teleport %s %s %s' % (dimension, ship_name, delta(x_tp), delta(y_tp), delta(z_tp))
	else:
		print '/execute as @a[tag=%s] at @s run teleport %s %s %s' % (ship_name, delta(x_tp), delta(y_tp), delta(z_tp))



print "UP"
# dr = UP
# dr_dest_nums = (0, 1, 0)
# dr_drive1_nums = (0, 1, 0)
# dr_drive2_nums = (0, 1, 0)
# pillar_facing = 'north'
mk_cmds(
	UP, # dr
	(0, 1, 0), # dr_dest_nums
	'up', # pillar_facing
	SHIP_NAME
)
print '\n\n'

print "DOWN"
mk_cmds(
	DOWN, # dr
	(0, -1, 0), # dr_dest_nums
	'up', # pillar_facing
	SHIP_NAME
)
print '\n\n'

print "FORWARD"
mk_cmds(
	FORWARD, # dr
	(0, 0, -3), # dr_dest_nums
	'up',
	SHIP_NAME
)
print '\n\n'

print "PORT"
mk_cmds(
	PORT, # dr
	(-3, 0, 0), # dr_dest_nums
	'up', # pillar_facing
	SHIP_NAME
)
print '\n\n'

print "STARBOARD"
mk_cmds(
	STARBOARD, # dr
	(3, 0, 0), # dr_dest_nums
	'up', # pillar_facing
	SHIP_NAME
)
print '\n\n'

print "REVERSE"
mk_cmds(
	REVERSE, # dr
	(0, 0, 3), # dr_dest_nums
	'up', # pillar_facing
	SHIP_NAME
)
print '\n\n'

print "NETHER"
mk_cmds(
	NETHER, # dr
	(0, 0, 0), # dr_dest_nums
	'down', # pillar_facing
	SHIP_NAME,
	dimension='the_nether',
)
print '\n\n'

print "OVERWORLD"
mk_cmds(
	OVERWORLD, # dr
	(0, 0, 0), # dr_dest_nums
	'down', # pillar_facing
	SHIP_NAME,
	dimension='overworld',
)
print '\n\n'
