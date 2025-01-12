class institution:
    # different copies for different objects
    def student_details(self,name,emailid,number):
        print(name,emailid,number)

    # static method decorator
    @staticmethod #this method can be accessed without creating the objects
    # also used to create utilities/ utilities functions
    # same copy shared by all th objects
    def mentor_class(list_mentor):
        print(list_mentor)


institution.mentor_class(["aneeqah","haamizah","junaid"])

    