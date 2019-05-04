import sys
import json

from k_means_algo import k_means


def write_cluster_to_file(output_file, clusters):
    for k in clusters:
        write_line = str(k) + '\t'
        for textID in clusters[k]:
            write_line += str(textID) + ", "
        output_file.write(write_line + "\n")


# Main Function
if __name__=="__main__":
     #check arguments validity
    # if len(sys.argv) != 5:
    #     print("Not enough arguments provided")
    #     sys.exit(0)


    #Read the files

    #num_of_centroids, seed_path, text_path, output_path = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    # seed_path = input("Enter seed path: ")
    # text_path = input("Enter texts path: ")
    # num_of_centroids = int(input("Enter centroid value: "))
    # output_path = input("Enter output path: ")

    seed_path = "./data/initial_seeds_3.txt"
    text_path = "./data/tweets_3.json"
    num_of_centroids = 3
    output_path = "./data"

    print("Number of centroids: {}".format(int(num_of_centroids)))
    texts = {} #texts is a dictionary
    #creating a dictionary with key as text id and value as text
    with open(text_path) as tf:
        for line in tf:
            print("Line: {}".format(line))
            text = json.loads(line)
            print("text: {}".format(text))
            texts[text['id']] = text


    seeds = []
    with open(seed_path) as sf:
        for line in sf:
            seeds.append(int(line.rstrip(',\n')))
    print(str(seeds))

    #We now have a texts dictionary and a seed list

    #clusters, id_with_clusters = k_means(seeds,texts,num_of_centroids)
    k_means(seeds, texts, num_of_centroids)

    # Writing to file

    # output_file = open(output_path,"w")
    # write_cluster_to_file(output_file, clusters)
    # output_file.close()



