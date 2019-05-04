from nltk.corpus import stopwords
import re, string
MAXITERATIONS = 4


def print_cluster(clusters):

    for key, value in clusters.items():
        print(key, str(value))

def update_clusters(texts, clusters, id_with_clusters, jaccard_table, num_centroids):

    k = num_centroids

    # Initialize new clusters

    updated_clusters, updated_id_with_clusters = {}, {}

    for k in range(k):
        updated_clusters[k] = set() # create a new set to hold updated clusters

    for text1 in texts:

        print("Text id => Text", text1, texts[text1])
        min_distance = float("inf") # infinite distance. minimize this distance metri using jaccard distance
        min_cluster = id_with_clusters[text1] # get the cluster to which this text currently belongs

        # Calculate min avg distance to each cluster

        for k in clusters: #there are default 3 clusters loop for each cluster and find the cluster with the min distance
            print("k: ", k)
            distance, total = 0, 0

            for text2 in clusters[k]: # calculate distance from each text in the cluster
                print("Text id in cluster => Text in cluster", text2)
                print("text1 and text2", text1, text2)
                distance += jaccard_table[text1][text2] # we have already calculated the distance between the two texts. we are just fetching it here
                total += 1
            print("distance", distance)
            print("total", total)
            if total > 0:
                average_distance = float(distance/ total)
                if average_distance < min_distance:
                    min_distance = average_distance
                    min_cluster = k # this is the ne min cluster for the text
        updated_id_with_clusters[text1] = min_cluster # after looping through all the cluster assign the new min cluster to the text id
        updated_clusters[min_cluster].add(text1) # add the text to the cluster dictionary, which contains the set of texts belonging to it

    return updated_clusters, updated_id_with_clusters




def find_stable_clusters(texts, clusters, id_with_clusters, jaccard_table, max_iterations, num_centroids):
    #initialize previous cluster to compare with new clustering
    updated_clusters, updated_id_with_clusters = update_clusters(texts, clusters, id_with_clusters, jaccard_table, num_centroids)

    # the above function call has given us the updated clusters and updated id_with_clusters
    #assign the new values to old as below
    clusters = updated_clusters
    id_with_clusters = updated_id_with_clusters

    #converge until old and new are same
    iterations = 1
    while iterations < max_iterations:
        updated_clusters, updated_id_with_clusters = update_clusters(texts, clusters, id_with_clusters, jaccard_table,num_centroids)
        iterations += 1
        if id_with_clusters != updated_id_with_clusters:
            print("Not converged yet..")
            clusters = updated_clusters
            id_with_clusters = updated_id_with_clusters
        else:
            print("Converged at ", iterations, " iterartions")
        return clusters, id_with_clusters

    # if meets max iterations, cut off the algo
    print("Meet max iterations")
    return clusters, id_with_clusters



def initialize_clusters(texts, seeds, num_of_centroids):
    clusters = {} # Stores cluster points (text ids) (cluster -> text id)
    id_with_clusters = {} # one to one mapping of id to cluster text (text id -> cluster)

    # Initially all texts are assigned no clusters
    for ID in texts: id_with_clusters[ID] = -1000 #cluster assigned to each ID is -1000

    # Initialize the clusters with the seeds from the file
    k = num_of_centroids
    for k in range(k):
        print("Seeds: ", str(seeds[k]))
        clusters[k] = set([seeds[k]])  # a list of sets. Cluster k is assigned a seed id
        id_with_clusters[seeds[k]] = k # seeds[k] is the text id..we are associating the text id with a cluster k
    print("Cluster: ", str(clusters))
    print("id_with_clusters: ", str(id_with_clusters))

    return clusters, id_with_clusters




# Calculates the Jaccard distance of a tweet using set notation
def jaccard_distance(set_one, set_two):
    return 1 - float(len(set_one.intersection(set_two))) / float(len(set_one.union(set_two)))


def create_bag_of_words(text):
    stop_words = stopwords.words("english")
    text_lower_case = text.lower()
    line = text_lower_case.split(" ")
    sentence = [] # empty list
    regex = re.compile("[%s]" % re.escape(string.punctuation))
    for word in line:
        word = word.strip()
        if not re.match(r'^https?:\/\/.*[\r\n]*', word) and word != '' and not re.match('\s',word) and word != 'rt' and not re.match('^@.*', word) and word not in stop_words:
            clean_word = regex.sub("", word)
            sentence.append(clean_word)
    print("Printing Sentence: ", str(sentence))
    return sentence



#Calculate the Jaccard distance between each pair of tweet. This will save up time
def initialize_jaccard_table(texts):
    jaccard_table = {} # this is a dictionary #key =id value = dictionary of distances from each other text

    #For each text in the texts list
    for textone in texts:
        jaccard_table[textone] = {} #key =text value = dictionary
        text_bag_words_one = set(create_bag_of_words(texts[textone]["text"]))
        #the above will return a bag of words for the text passed in the parameter

        #Now compare the above bag of words to other texts

        for texttwo in texts:
            if texttwo not in jaccard_table:
                jaccard_table[texttwo] = {}
            text_bag_words_two = set(create_bag_of_words(texts[texttwo]["text"]))
            jaccard_dist = jaccard_distance(text_bag_words_one,text_bag_words_two)
            jaccard_table[textone][texttwo], jaccard_table[textone][texttwo] = jaccard_dist, jaccard_dist
    print("printing jaccard table", str(jaccard_table))
    return jaccard_table




def k_means_set_up(seeds,texts,num_of_centroids):
    #create_bag_of_words(texts) -- this function should get called only once. curently gettng called repeatedly
    jaccard_table = initialize_jaccard_table(texts)
    clusters, id_with_clusters = initialize_clusters(texts, seeds, num_of_centroids)
    return jaccard_table, clusters, id_with_clusters

#Run kmeans algorithm on text
def k_means(seeds,texts,num_of_centroids):

    #initialize a look up table to calculate all the jaccard distances pairs. initialize all clusters
    jaccard_table,clusters, id_with_clusters = k_means_set_up(seeds,texts,num_of_centroids)

    # Run k-means algo

    clusters, id_with_clusters = find_stable_clusters(texts, clusters, id_with_clusters, jaccard_table, MAXITERATIONS, num_of_centroids)
    # prints results to screen

    print_cluster(clusters)
