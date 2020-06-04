class mod_lua():
	def __init__(self, file):
		# open file
		self.f_id = open(file,"r+")
		#self.lines = self.f_id.readlines()

	def get_value(self,var):
		self.f_id.seek(0)
		line, _ = self.__lookupVar(var)
		self.f_id.seek(0)
		if not line:
			return None
		
		RHS = line.split("=")[1]
		RHS_split = RHS.split(" ")
		for x in RHS_split:
			if x:
				return x.split(" ")[0].split("\t")[0]

	def set_value(self, var, value):
		line, i = self.__lookupVar(var)
		if not line:
			return None
		self.f_id.seek(0)
		content = self.f_id.readlines()
		#print(line)
		#print(content[i])

		content[i] = line.split("=")[0] + " = " + str(value) + "\n"
		#print(content[i])

		# delete content
		self.f_id.seek(0)
		self.f_id.truncate()
		# rewrite everything
		self.f_id.writelines(content)

	def close(self):
		self.f_id.close()

	def __lookupVar(self, var):
		i = 0
		for line in self.f_id:
			if var in line:
				return line, i
			i += 1
		return False, i


def main():
	file = "C:/Users/cesar/Documents/CU Robotics/Software/Lua_rw_class/2_ouster_test.lua"
	test = mod_lua(file)
	# test get value
	print(test.get_value("MAX_3D_RANGE"))
	#print(test.get_value("TRAJECTORY_BUILDER_3D.submaps.range_data_inserter.miss_probability"))
	print(test.get_value("POSE_GRAPH.constraint_builder.ceres_scan_matcher_3d.only_optimize_yaw"))

	# test set value
	test.set_value("TRAJECTORY_BUILDER_3D.min_range", 5.1)
	#print(test.get_value("TRAJECTORY_BUILDER_3D.min_range"))


	test.close()



if __name__ == '__main__':
	main()