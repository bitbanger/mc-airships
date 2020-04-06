LNW = (127, 70, -294)
USE = (135, 75, -280)

PORT = (115, 76, -285)
REVERSE = (117, 76, -285)
STARBOARD = (119, 76, -285)
UP = (118, 76, -281)
DOWN = (116, 76, -281)
FORWARD = (131, 70, -294)

def to_lnw(blk):
	return (LNW[0]-blk[0], LNW[1]-blk[1], LNW[2]-blk[2])

def to_use(blk):
	return (USE[0]-blk[0], USE[1]-blk[1], USE[2]-blk[2])

def delta(n):
	if n == 0:
		return '~'
	else:
		return '~%d' % (n)



def mk_cmds(dr, dr_dest_nums, dr_drive1_nums, dr_drive2_nums, dr_drive_facing):
	drive1 = (dr[0] + dr_drive1_nums[0], dr[1] + dr_drive1_nums[1], dr[2] + dr_drive1_nums[2])
	dr_lnw_delt = [delta(x) for x in to_lnw(drive1)]
	dr_use_delt = [delta(x) for x in to_use(drive1)]
	dr_dest_delt = [delta(to_lnw(drive1)[i] + dr_dest_nums[i]) for i in range(len(dr_dest_nums))]
	print '/setblock %s %s %s minecraft:command_block[facing=%s]{%sCommand:"/clone %s %s %s %s %s %s %s %s %s replace move"}' % tuple([delta(dr_drive1_nums[0]), delta(dr_drive1_nums[1]), delta(dr_drive1_nums[2]), dr_drive_facing, 'auto:1,' if dr == UP or dr == FORWARD else ''] + dr_lnw_delt + dr_use_delt + dr_dest_delt)
	
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

print "UP"
# dr = UP
# dr_dest_nums = (0, 1, 0)
# dr_drive1_nums = (0, 1, 0)
# dr_drive2_nums = (0, 1, 0)
# dr_drive_facing = 'north'
mk_cmds(
	UP, # dr
	(0, 1, 0), # dr_dest_nums
	(0, 2, 0), # dr_drive1_nums
	(0, 2, 0), # dr_drive2_nums
	'north' # dr_drive_facing
)
print '\n\n'

print "DOWN"
mk_cmds(
	DOWN, # dr
	(0, -1, 0), # dr_dest_nums
	(0, 1, 0), # dr_drive1_nums
	(0, 1, 0), # dr_drive2_nums
	'north' # dr_drive_facing
)
print '\n\n'

print "FORWARD"
mk_cmds(
	FORWARD, # dr
	(0, 0, -1), # dr_dest_nums
	(0, 0, -2), # dr_drive1_nums
	(0, 0, -2), # dr_drive2_nums
	'east' # dr_drive_facing
)
print '\n\n'

print "PORT"
mk_cmds(
	PORT, # dr
	(-1, 0, 0), # dr_dest_nums
	(0, 1, 0), # dr_drive1_nums
	(0, 1, 0), # dr_drive2_nums
	'south' # dr_drive_facing
)
print '\n\n'

print "STARBOARD"
mk_cmds(
	STARBOARD, # dr
	(1, 0, 0), # dr_dest_nums
	(0, 1, 0), # dr_drive1_nums
	(0, 1, 0), # dr_drive2_nums
	'south' # dr_drive_facing
)
print '\n\n'

print "REVERSE"
mk_cmds(
	REVERSE, # dr
	(0, 0, 1), # dr_dest_nums
	(0, 1, 0), # dr_drive1_nums
	(0, 1, 0), # dr_drive2_nums
	'south' # dr_drive_facing
)
print '\n\n'
