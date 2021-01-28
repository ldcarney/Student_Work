# CS1300 Fall 2017
# Author: Liam Carney

#reading through text file

def read_users(file_name):
	user = {}
	try:
		f = open(file_name)
		for line in f:
			ratings = [ ]
			line = line.strip().split()
			name = line[0]
			for i in line [1:]:
				ratings.append (int(i))
			user[name] = ratings
		return user 
	except:
		return None
def read_books(file_name):
	read = []
	try:
		f = open(file_name)
		for line in f:
			line = line.strip() .split(',')
			read.append([line[1], line[0]])
			#book_list[0] = line
		return read
	except :
		return None
def calculate_average_rating(user):
	list = []
	users = user.keys()
	ind = users[0]
	for i in range(len(user[ind])):
		count = 0
		sum1 = 0
		for u in users:
			if user[u][i] != 0:
				sum1 = sum1 + user[u][i]
				count = count + 1
		avg = sum1/float(count)
		print(avg)
		list.append(avg)
	return list

def lookup_average_rating(book_index, book_list, ave_rating_list):
	return ("({:.2f}) {} by {}").format(ave_rating_list[book_index], book_list[book_index][0],book_list[book_index][1])

#PART_2 follow here

class Recommender:
	#Constructor here
	def __init__(self, file_name, user_file):
		self.book_list = []
		self.user_dictionary = {}
		self.average_rating_list = []

		self.read_books(file_name)
		self.read_users(user_file)
		self.calculate_average_rating()

	def read_books(self, file_name):
		try:
			f = open(file_name)
			for line in f:
				line = line.strip().split(',')
				self.book_list.append([line[1], line[0]])

		except IOError as e:
			return None

	def read_users(self, file_name):

		try:
			f = open(file_name)
			for line in f:
				ratings = [ ]
				line = line.strip().split()
				name = line[0]
				for i in line[1:]:
					ratings.append(int(i))
					self.user_dictionary[name] = ratings
		except IOError as e:
			return None

	def calculate_average_rating(self):

		self.average_rating_list = []
		users = self.user_dictionary.keys()
		ind = users[0]
		for i in range(len(self.user_dictionary[ind])):
			count = 0
			sum1 = 0
			for u in users:
				if self.user_dictionary[u][i] != 0:
					sum1 = sum1 + self.user_dictionary[u][i]
					count1 = count + 1
			avg = sum1/float(count)
			print(avg)
			self.average_rating_list.append(avg)
		return self.average_rating_list

	def lookup_average_rating(self, book_index):

		return ("({:.2f}) {} by {}").format(self.average_rating_list[book_index], self.book_list[book_index][0], self.book_list[book_index][1])

	def calc_similarity(self, user1, user2):

		r1 = self.user_dictionary[user1]
		r2 = self.user_dictionary[user2]
		dp = 0

		for i in range (len(r1)):
			dp = dp + r1[i] * r2[i]
		return dp

	def get_most_similar_user(self, current_user_id):
		highest = 0
		best_matched = ""
		users = self.user_dictionary.keys()
		for user in users:
			if user != current_user_id:
				score = self.calc_similarity(user, current_user_id)
				if score > highest:
					highest = score
					best_matched = user
		return best_matched

	def recommend_books(self, current_user_id):

		return recommendations_list

def main():
	book_list = read_books("book.txt")
	user_dict = read_users("ratings.txt")
	ave_rating_list = calculate_average_rating(user_dict)
	print(lookup_average_rating(0, book_list, ave_rating_list))

if __name__ == "__main__":
	main()

