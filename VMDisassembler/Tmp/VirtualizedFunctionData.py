from FinSpyVM import *

NOT_VIRTUALIZED = set([
0x0040a07c,
0x0040ae80,
0x0040709e,
0x0040ae74,
0x0040aec7,
0x004070d8,
0x00407119,
0x00401935,
0x00408150,
0x00407155,
])

# Get the targets of all X86CALLOUT instructions
# Also takes the vmEntrypoint, since it won't be called
def ExtractCalloutTargets(insns, vmEntrypoint):
	# Python scoping statement
	global ALL_FIXED_UP_DWORDS
	
	# Initialize the set to the function pointer 
	# addresses collected in ApplyFixup
	#calloutTargets = set(ALL_FIXED_UP_DWORDS.keys())
	calloutTargets = set([])
	
	# Add vmEntrypoint to set
	calloutTargets.add(vmEntrypoint)
	
	# Extract X86CALLOUT targets
	for i in insns:
		if isinstance(i,RawX86Callout):
			if i.X86Target not in NOT_VIRTUALIZED:
				calloutTargets.add(i.X86Target)
	
	# Existing: return list of targets
	return list(calloutTargets)

# Address of WinMain in sample
WINMAIN_VIRTUALIZED_ADDRESS = 0x00406154
	
# Run this as-needed to generate code for function prologue extraction
# Disassemble and simplify VM bytecode program
#newInsns = list(bytes_from_file("Tmp/dec.bin"))
#print repr(ExtractCalloutTargets(newInsns, WINMAIN_VIRTUALIZED_ADDRESS))

KEY_TO_X86_VMENTRY_AND_KEY_TO_X86_VMENTRY_AND_PROLOGUE_BYTES_TUPLES = [
# MANUALLY-ADDED ENTRIES:
(0x5A2A19,0x405022,[0x8B,0x65,0xE8,0xC7,0x45,0xC0,0x01,0x00,0x00,0x00,0x83,0x4D,0xFC,0xFF,0x33,0xF6]),
(0x5A3FA0,0x4060E6,[]),
(0x5A6841,0x408053,[]),
(0x5A6958,0x408107,[]),
(0x5A6AE9,0x408290,[]),
(0x5A6D38,0x40840D,[]),
(0x5A6ED6,0x40851C,[0x8B,0xFF,0x55,0x8B,0xEC]),
(0x5A7952,0x408D0C,[0x8B,0xFF]),

# AUTOMATICALLY-GENERATED ENTRIES
(0x5a4b3a, 0x406a02, [139, 255, 85, 139, 236, 81, 81, 83, 86, 87]),
(0x5a19e6, 0x40171c, [85, 139, 236]),
(0x5a7a1d, 0x408e07, [139, 255, 85, 139, 236, 81, 131, 101, 252, 0]),
(0x5a3783, 0x405a0e, [139, 255, 85, 139, 236]),
(0x5a7314, 0x408810, [139, 255, 85, 139, 236, 81, 81]),
(0x5a8bf9, 0x409a11, [139, 255, 85, 139, 236, 83, 86, 87, 179, 254]),
(0x5a781e, 0x408c14, [139, 255, 85, 139, 236]),
(0x5a658d, 0x407e15, [139, 255, 85, 139, 236, 86]),
(0x5a4e2f, 0x406c16, [139, 255, 85, 139, 236, 129, 236, 72, 8, 0, 0, 83, 86, 51, 246, 87, 137, 117, 220, 137, 117, 224, 137, 117, 216]),
(0x5a187e, 0x401617, [85, 139, 236]),
(0x5a35c6, 0x40581e, [139, 255, 85, 139, 236]),
(0x5a27b6, 0x404e1f, [139, 255, 85, 139, 236, 131, 236, 28, 83, 86, 87]),
(0x5a1b63, 0x401821, [85, 139, 236]),
(0x5a6e30, 0x4084b2, [139, 255, 85, 139, 236, 86]),
(0x5a98f7, 0x40a63e, [139, 255, 85, 139, 236, 129, 236, 52, 11, 0, 0, 86, 51, 246, 87, 137, 117, 240, 137, 117, 252, 137, 117, 244, 137, 117, 248, 198, 69, 228, 0, 198, 69, 229, 0, 198, 69, 230, 0, 198, 69, 231, 0, 198, 69, 232, 0, 198, 69, 233, 16, 137, 117, 236]),
(0x5a7a4a, 0x408e3f, [139, 255, 85, 139, 236, 81, 81, 83, 86, 87]),
(0x5a37b6, 0x405a44, [139, 255, 85, 139, 236]),
(0x5a35e6, 0x405847, [139, 255, 85, 139, 236]),
(0x5a7855, 0x408c4e, [139, 255, 85, 139, 236, 131, 236, 16, 51, 201, 51, 210]),
(0x5a4750, 0x406653, [139, 255, 85, 139, 236, 129, 236, 112, 4, 0, 0, 86, 51, 246, 87, 137, 117, 240]),
(0x5a16da, 0x40150e, [85, 139, 236]),
(0x5a735e, 0x408857, [139, 255, 85, 139, 236, 81, 81]),
(0x5a608c, 0x407a58, [139, 255, 85, 139, 236, 129, 236, 80, 2, 0, 0, 87, 51, 255, 137, 125, 252]),
(0x5a5b37, 0x40765a, [139, 255, 83, 86, 87, 51, 255]),
(0x5a7b88, 0x408f0f, [139, 255, 87]),
(0x5a558f, 0x407261, [139, 255, 85, 139, 236, 131, 236, 16, 83, 86, 87]),
(0x5a8ef5, 0x409c62, [139, 255, 85, 139, 236, 129, 236, 40, 2, 0, 0, 83, 51, 219, 137, 93, 240, 137, 93, 236]),
(0x5a65f6, 0x407e65, [139, 255, 85, 139, 236, 86]),
(0x5a1bc7, 0x401866, [85, 139, 236]),
(0x5a8c77, 0x409a67, [139, 255, 85, 139, 236]),
(0x5a1901, 0x40166e, [85, 139, 236]),
(0x5a1cab, 0x404670, [85, 139, 236]),
(0x5a4bc8, 0x406a74, [139, 255, 85, 139, 236, 81, 81, 83, 86, 87]),
(0x5a1664, 0x4014be, [85, 139, 236]),
(0x5a70b7, 0x40867a, [139, 255, 85, 139, 236]),
(0x5a69bd, 0x4081c0, [139, 255, 85, 139, 236, 129, 236, 36, 3, 0, 0, 83, 87]),
(0x5a37fd, 0x405a8e, [139, 255, 85, 139, 236]),
(0x5a362d, 0x405891, [139, 255, 85, 139, 236]),
(0x5a15ff, 0x40146e, [85, 139, 236]),
(0x5a8cad, 0x409a97, [139, 255, 85, 139, 236, 129, 236, 8, 1, 0, 0, 83, 86, 87]),
(0x5a1cc3, 0x404698, [139, 255, 85, 139, 236, 81, 83, 87]),
(0x5a6435, 0x407c9f, [139, 255, 85, 139, 236, 129, 236, 28, 2, 0, 0, 83, 86]),
(0x5a7dc8, 0x4090a7, [139, 255, 85, 139, 236, 129, 236, 36, 2, 0, 0, 86]),
(0x5a2dd1, 0x4052a9, [139, 255, 85, 139, 236, 129, 236, 36, 2, 0, 0, 83, 86, 87]),
(0x5a1c0f, 0x4018ab, [85, 139, 236]),
(0x5a8716, 0x4096b1, [139, 255, 85, 139, 236, 129, 236, 12, 2, 0, 0, 83, 86, 87]),
(0x5a68c6, 0x4080b2, [139, 255, 85, 139, 236, 83, 86, 87]),
(0x5a3f52, 0x4060b3, [139, 255, 85, 139, 236, 131, 236, 64, 87]),
(0x5a1586, 0x40141e, [85, 139, 236]),
(0x5a78e0, 0x408cbe, [139, 255, 85, 139, 236, 131, 236, 32]),
(0x5a5bc4, 0x4076c2, [139, 255, 85, 139, 236, 129, 236, 68, 4, 0, 0, 83, 86, 87]),
(0x5a3646, 0x4058c3, [139, 255, 85, 139, 236]),
(0x5a3824, 0x405ac4, [139, 255, 85, 139, 236]),
(0x5a196b, 0x4016c5, [85, 139, 236]),
(0x5a3114, 0x4054c8, [139, 255, 85, 139, 236, 129, 236, 100, 4, 0, 0, 83, 86, 87]),
(0x5a6682, 0x407ec9, [139, 255, 85, 139, 236, 139, 77, 8, 86]),
(0x5a769d, 0x408acc, [139, 255, 85, 139, 236, 131, 236, 36]),
(0x5a5634, 0x4072ce, [139, 255, 85, 139, 236, 129, 236, 36, 2, 0, 0, 83, 86, 87]),
(0x5a73f3, 0x4088d5, [139, 255, 85, 139, 236]),
(0x5a9291, 0x409edc, [139, 255, 85, 139, 236, 86, 87]),
(0x5a4c91, 0x406ae6, [139, 255, 85, 139, 236, 129, 236, 112, 2, 0, 0, 83, 86, 87, 51, 219]),
(0x5a812b, 0x4092e7, [139, 255, 85, 139, 236, 129, 236, 64, 2, 0, 0, 83]),
(0x5a1c58, 0x4018f0, [85, 139, 236]),
(0x5a92ea, 0x409f2b, [139, 255, 85, 139, 236, 131, 236, 28, 83, 51, 219, 86, 137, 93, 252, 137, 93, 248, 51, 246, 137, 93, 244, 136, 93, 228, 136, 93, 229, 136, 93, 230, 136, 93, 231, 136, 93, 232, 198, 69, 233, 5, 137, 93, 236]),
(0x5a7419, 0x408904, [139, 255, 85, 139, 236]),
(0x5a718f, 0x40870b, [139, 255, 85, 139, 236, 131, 236, 32, 83, 86, 87]),
(0x5a3699, 0x40590d, [139, 255, 85, 139, 236]),
(0x5a387c, 0x405b0e, [139, 255, 85, 139, 236]),
(0x5a66d1, 0x407f0f, [139, 255, 85, 139, 236]),
(0x5a6972, 0x40811c, [139, 255, 85, 139, 236]),
(0x5a795f, 0x408d2b, [139, 255, 85, 139, 236]),
(0x5a7717, 0x408b2c, [139, 255, 85, 139, 236, 131, 236, 36]),
(0x5a7440, 0x408933, [139, 255, 85, 139, 236, 129, 236, 68, 6, 0, 0, 83, 86, 87]),
(0x5a36bd, 0x40593c, [139, 255, 85, 139, 236]),
(0x5a6eeb, 0x408540, [139, 255, 85, 139, 236]),
(0x5a38af, 0x405b44, [139, 255, 85, 139, 236]),
(0x5a1de8, 0x404747, [139, 255, 85, 139, 236, 129, 236, 96, 12, 0, 0, 86, 87, 51, 255]),
(0x5a7bb9, 0x408f4b, [139, 255, 85, 139, 236, 129, 236, 52, 2, 0, 0, 83, 86, 87]),
(0x5a2991, 0x404f4c, [139, 255]),
(0x5a6719, 0x407f53, [139, 255, 85, 139, 236]),
(0x5a403d, 0x406154, [139, 255, 85, 139, 236, 129, 236, 148, 12, 0, 0, 83, 86, 87]),
(0x5a4a6d, 0x406958, [139, 255, 85, 139, 236]),
(0x5a7991, 0x408d5d, [139, 255, 85, 139, 236]),
(0x5a6c26, 0x408360, [139, 255, 85, 139, 236, 129, 236, 32, 3, 0, 0, 83, 87]),
(0x5a1767, 0x401562, [85, 139, 236]),
(0x5a1a5e, 0x401765, [85, 139, 236]),
(0x5a850f, 0x409567, [139, 255, 85, 139, 236, 131, 236, 12, 86]),
(0x5a1475, 0x401370, [85, 139, 236]),
(0x5a36f3, 0x405972, [139, 255, 85, 139, 236]),
(0x5a23b6, 0x404b76, [139, 255, 85, 139, 236, 81, 131, 101, 252, 0]),
(0x5a29ac, 0x404f77, [104, 108, 11, 0, 0, 104, 112, 183, 64, 0, 232, 6, 95, 0, 0, 51, 246, 137, 117, 224]),
(0x5a38e5, 0x405b7a, [139, 255, 85, 139, 236]),
(0x5a6f32, 0x40857e, [139, 255, 85, 139, 236, 83, 86, 87]),
(0x5a145d, 0x401340, [85, 139, 236]),
(0x5a7785, 0x408b8c, [139, 255, 85, 139, 236, 86]),
(0x5a79c2, 0x408d8f, [139, 255, 85, 139, 236, 86]),
(0x5a4aa0, 0x406996, [139, 255, 85, 139, 236]),
(0x5a94a9, 0x40a19a, [139, 255, 85, 139, 236, 129, 236, 80, 7, 0, 0, 83, 86, 51, 219, 87, 137, 93, 232]),
(0x5a5767, 0x4073a2, [139, 255, 85, 139, 236, 129, 236, 64, 8, 0, 0, 83, 86, 87]),
(0x5a5497, 0x4071a3, [139, 255, 85, 139, 236, 86]),
(0x5a3723, 0x4059a5, [139, 255, 85, 139, 236]),
(0x5a17ed, 0x4015b2, [85, 139, 236]),
(0x5a6794, 0x407fb4, [139, 255]),
(0x5a1acb, 0x4017b5, [85, 139, 236]),
(0x5a464e, 0x4065b8, [139, 255, 85, 139, 236, 131, 236, 24, 131, 101, 248, 0, 86]),
(0x5a73b7, 0x40889f, [139, 255, 85, 139, 236]),
(0x5a88c4, 0x4097f5, [139, 255, 85, 139, 236, 129, 236, 16, 5, 0, 0, 83, 86, 87]),
(0x5a14eb, 0x4013c0, [85, 139, 236]),
(0x5a2411, 0x404bc2, [139, 255, 85, 139, 236, 131, 236, 24, 83, 51, 219, 136, 93, 232, 136, 93, 233, 136, 93, 234, 136, 93, 235, 136, 93, 236, 198, 69, 237, 5]),
(0x5a3943, 0x405bc4, [139, 255, 85, 139, 236, 129, 236, 48, 6, 0, 0, 83, 86, 87, 51, 255, 137, 125, 232]),
(0x5a8e33, 0x409bc8, [139, 255, 85, 139, 236]),
(0x5a4ae9, 0x4069ca, [139, 255, 85, 139, 236]),
(0x5a79fa, 0x408dce, [139, 255, 85, 139, 236, 81, 131, 101, 252, 0]),
(0x5a329b, 0x4055d5, [139, 255, 85, 139, 236]),
(0x5a3755, 0x4059db, [139, 255, 85, 139, 236]),
(0x5a77fc, 0x408bde, [139, 255, 85, 139, 236]),
(0x5a6fc1, 0x4085e7, [139, 255, 85, 139, 236]),
(0x5a54fe, 0x4071f4, [139, 255, 85, 139, 236, 131, 236, 16, 83, 86, 87]),
(0x5a67e7, 0x407ff5, [139, 255, 85, 139, 236, 131, 236, 12]),
(0x5a8e58, 0x409bf7, [139, 255, 85, 139, 236, 83, 86, 87]),
(0x5a32ba, 0x4055fe, [139, 255, 85, 139, 236, 129, 236, 216, 6, 0, 0, 83, 86, 51, 219, 87, 137, 93, 248]),
]
