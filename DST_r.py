
class node:
	def __init__(self, range_bits,node_length,headsh,key_length):
		self.range_bits = range_bits << node_length # pad range_bits
		self.node_length = node_length
		self.head_shift = headsh
		self.key_length = key_length
		self.num_shifts = (self.key_length-self.node_length)/self.head_shift
		self.values = {}
		#table containing masked bit ranges associated with other nodes
		self.f_table = {}
		
	def get_value(self, key):
		rbm = 0 #to store range bitmasked
		kbm = 0#to store key bitmasked
		bitmask = (2^self.head_shift - 1) #fill with correct number of ones
		bitmask = bitmask << (self.node_length + (self.num_shifts-1)*self.head_shift) #skip over node stored bits
		#todo skip over alread processed bits
		for i in range(0,self.num_shifts):
			rbm = self.range_bits&bitmask
			kbm = key&bitmask
			print("offset %i" %i)
			print("bitmask: %s" %bin(bitmask))
			print("rbm: %s" %bin(rbm))
			print("kbm: %s" %bin(kbm))
			if rbm == kbm:
				bitmask = bitmask >> (self.head_shift)
			else:
				print("value not found contact other node")
				if kbm in self.f_table:
				  return (False,self.f_table[kbm])#wrong place link to right
				else:
				  return (False,False)#wrong place, link not found
		#if it gets here key is in node's range check table
		if key in self.values:
		  return (True,self.values[key])#right place found value
		else:
		  return (True,False)#right place value not found

	def add_value(self,key,value):
	  #todo check if it is in range
	  self.values[key]=value
	def add_finger(self,f_address,f_range):
	  self.f_table[f_range] = f_address;
		
nodes = {}
def query_node(node_num,key):
  address = node_num
  while(True):
    v_found, v = nodes[address].get_value(key)
    if v_found == True:
      return v
    elif(v == False):
      print("value not in table")
      return v
    else:
      print("gonig to node %i" %v)
      address = v
  
nodes[0] = node(int('001011',2),2,2,8)
nodes[0].add_value(int('00101110',2),True)
nodes[0].add_finger(1,int('00010000',2))

nodes[1] = node(int('000111',2),2,2,8)
nodes[1].add_value(int('00011110',2),True)

print query_node(0,int('00101110',2))#hit
print query_node(0,int('00011110',2))#miss on 0 hit on 1