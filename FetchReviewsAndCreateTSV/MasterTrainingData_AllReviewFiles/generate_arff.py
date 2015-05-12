import sys
TEST_DATA_PATH = sys.argv[2] 
TRAIN_DATA_PATH = sys.argv[1] 


def parse_data(train_data, test_data):
    """
    Input: path to the data file
    Output: (1) a list of tuples, one for each instance of the data, and
            (2) a list of all unique tokens in the data

    Parses the data file to extract all instances of the data as tuples of the form:
    (person, review, judgment, full snippet, intermediate text)
    where the intermediate text is all tokens that occur between the first occurrence of
    the person and the first occurrence of the review.

    Also extracts a list of all tokens that appear in the intermediate text for the
    purpose of creating feature vectors.
    """
    all_tokens = []
    data = []
    for fp in [train_data, test_data]:
        with open(fp) as f:
            for line in f:
                title, location, review, judgment = line.split("\t")
                judgment = judgment.strip()

                # Build up a list of unique tokens that occur in the intermediate text
                # This is needed to create BOW feature vectors
                tokens = review.split()
                for t in tokens:
                    t = t.lower()
                    if t not in all_tokens:
                        all_tokens.append(t)
                data.append((review, judgment))
    return data, all_tokens


def create_feature_vectors(data, all_tokens):
    """
    Input: (1) The parsed data from parse_data()
             (2) a list of all unique tokens found in the intermediate text
    Output: A list of lists representing the feature vectors for each data instance

    Creates feature vectors from the parsed data file. These features include
    bag of words features representing the number of occurrences of each
    token in the intermediate text (text that comes between the first occurrence
    of the person and the first occurrence of the review).
    This is also where any additional user-defined features can be added.
    """
    feature_vectors = []
    for instance in data:
        try:
	        # BOW features
	        # Gets the number of occurrences of each token
	        # in the intermediate text
	        feature_vector = [0 for t in all_tokens]
	        intermediate_text = instance[0]
	        tokens = intermediate_text.split()
	        for token in tokens:
	            index = all_tokens.index(token.lower())
	            feature_vector[index] += 1
	
	        ### ADD ADDITIONAL FEATURES HERE ###
	
        	# Class label
	        judgment = instance[1]
	        feature_vector.append(judgment)
	
	        feature_vectors.append(feature_vector)
	except:
		continue	
    return feature_vectors


def generate_arff_file(feature_vectors, all_tokens, out_path):
    """
    Input: (1) A list of all feature vectors for the data
             (2) A list of all unique tokens that occurred in the intermediate text
             (3) The name and path of the ARFF file to be output
    Output: an ARFF file output to the location specified in out_path

    Converts a list of feature vectors to an ARFF file for use with Weka.
    """
    with open(out_path, 'w') as f:
        # Header info
        f.write("@RELATION reviews\n")
        for i in range(len(all_tokens)):
            f.write("@ATTRIBUTE token_{} INTEGER\n".format(i))

        ### SPECIFY ADDITIONAL FEATURES HERE ###
        # For example: f.write("@ATTRIBUTE custom_1 REAL\n")

        # Classes
        f.write("@ATTRIBUTE class {1,2,3,4,5,6,7,8,9,10}\n")

        # Data instances
        f.write("\n@DATA\n")
        for fv in feature_vectors:
            features = []
            for i in range(len(fv)):
                value = fv[i]
                if value != 0:
                    features.append("{} {}".format(i, value))
            entry = ",".join(features)
            f.write("{" + entry + "}\n")

if __name__ == "__main__":
    data, all_tokens = parse_data(TRAIN_DATA_PATH, TEST_DATA_PATH)
    feature_vectors = create_feature_vectors(data, all_tokens)
    generate_arff_file(feature_vectors[:150], all_tokens, "train.arff")
    generate_arff_file(feature_vectors[150:], all_tokens, "test.arff")
