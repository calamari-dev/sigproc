pkg load statistics
csvwrite("./pca.csv", mvnrnd([0 0], [25 9; 9 16], 500))
