This guide countains instructions for how to run the combination of textural and acoustic features program for tag classification in Python.
The source code can be obtained through the GitHub repository: https://github.com/DouglasTanno/tag-annotation.git

The following steps are described:
- Feature Extraction (Acoustic and Textural Features);
- Stacking Generalization (First and Second Stage);
- Prediction Evaluation (Precision, Recall, Accuracy and F-Score);
- Combination (Early and Late Fusion).

The text files, countaining the input file paths (songs or images) of the used datasets must be randomly split into train (70%) and test (30%), resulting in the train.txt and test.txt files, respectively.

It is assumed that the train.txt is a training list file, countaining the file path and the respective tags for each training file, and the test.txt is a testing list file, countaining only the path for each testing file. 
Additionally, a tags.txt is also needed, countaining a list of all the possible tags used in the training file. The tags must be comma-delimited and should not be duplicated.
A file with the test.txt content plus the respective file tags is also needed for the results evaluation (e.g., test-tags.txt). 
It is important that all the files paths in the lists are correct for the feature extraction.



1. Feature Extraction:

Acoustic and textural features are extracted for further classification and combination.

1.1 Acoustic Features Extraction:

This step is executed using Marsyas 0.5.0, an open source software used for audio processing. More information available in marsyas.info.
The train.txt and test.txt files are used as input. As output, the train.arff and test.arff files are generated, countaining the acoustic features data. 
The features consist of means and variances of time-domain Zero-Crossings, Spectral Centroid, Rolloff, Flux and Mel-Frequency Cepstral Coefficients (MFCC) over a texture window of 1 sec.
For further instructions about this step, check ACM Multimedia 2009's paper "Improving Automatic Music Tag Annotation Using Stacked Generalization Of Probabilistic SVM Outputs".
The total output of features is 124.

Commands: 
> bextract -ws 1024 -as 400 -sv -fe train.txt -w train.arff -od /path/to/workdir/
> bextract -ws 1024 -as 400 -sv -fe test.txt -w test.arff -od /path/to/workdir/

These two commands will generate the respectively .arff file in the directory specified.

1.2 Textural Features Extraction:

The LBP features extraction is executed using the lbp_train.py and lbp_test.py scripts.
Both import the "localbinarypatterns" python script, located in the pyimagesearch folder (provided by http://pyimagesearch.com for texture and pattern identification and classification). The function "local_binary_pattern", provided by the skimage library, is used to extract the textural features from the input images.
The values of points and radius parameters for the LBP are already pre-determined as 2 and 122, respectively. Though, it can be modified as the user demands. 
The total output of features is 124.

The train.txt, test.txt and tags.txt files must be in the directory specified in the commands. 
If somehow the file is not found, the message "Error reading X file", being X the file name, will pop out and the script execution will be interrupted.

Commands:
> train.py /path/to/workdir/
> test.py /path/to/workdir/

These two commands will generate the respectively .arff file in the directory specified.



2. Stacking Generalization:

Stacking generalization consists of a two-stage execution, using a SVM Classifier to generate the tag classification predictions.
This step consists of using the "kea" function and the "threshold_binarization.rb" Ruby script from Marsyas, also specified by ACM Multimedia 2009's paper.

2.1 First Stage:

The .arff files generated in the previous steps are used as input.
In the first command specified below stage1_affinities.txt file will be generated. This file contains the predicted tag affinities of each song for all the tags in the test.txt.
The second command consists in generating the file stage1_predictions.txt, a predicted tag binary relevance file, through the execution of the threshold_binarization.rb script.

Commands:
> kea -m tags -id /path/to_working_dir -od /path/to/workdir -w train.arff -tc test.arff -pr stage1_affinities.txt 
> ../../scripts/Ruby/threshold_binarization.rb train.txt stage1_affinities.txt > stage1_predictions.txt

In addition, the stacked_train.arff and stacked_test.arff files are generated as well, to be used in the step 2.2.

2.2 Second Stage:

The stacked_train.arff and stacked_test.arff files generated in the previous steps are used as input.
The commands are similar to the those specified in the step 2.1. The stage2_affinities.txt and stage2_predictions.txt files are generated.

Commands:
> kea -m tags -id /path/to_workdir -od /path/to/workdir -w stacked_train.arff -tc stacked_test.arff -pr stage2_affinities.txt 
> ../../scripts/Ruby/threshold_binarization.rb train.txt stage2_affinities.txt > stage2_predictions.txt 



3. Prediction Evaluation:

After the completion of the two stages of stacking of the step 2, the prediction of both stages will be evaluated through the per-tag-and-global-precision-recall-fixed.rb Ruby script.
The results are evaluated through the metrics of Precision, Recall, Accuracy and F-Score.

Commands:
> ruby per-tag-and-global-precision-recall-fixed.rb test-tags.txt stage1_predictions.txt.txt
> ruby per-tag-and-global-precision-recall-fixed.rb test-tags.txt stage2_predictions.txt.txt



4. Combination:

Besides the preditions made with acoustic or textural features, this paper proposed two combinations of both features, for further evaluation of tag classifications predictions.

4.1 Early Fusion:

This step consists in combining the train.arff and test.arff generated in the steps 1.1 and 1.2, with the ef_train.py and ef_test.py scripts, respectively.
The train.arff and test.arff (248 features each), with the combination of the features of the input files, are generated in the script directory.

Commands:
> ef_train.py train_acoustic.arff train_lbp.arff train.txt
> ef_test.py test_acoustic.arff test_lbp.arff test.txt

After the combination, the resulting output files are used as input for the steps 2 and 3.

4.2 Late Fusion:

This step consists in combining both stage_affinities.txt of acoustic and textural features, generated in the step 2.1 and 2.2 separetely. 
Four combinations are made, based on the operations of Maximum, Minimum, Sum and Product, using the late_fusion.py. These operations are applied to each line of the stage_affinities.txt, resulting in four .txt output files, referring to each operation.

Commands:
> late_fusion.py ac_stage1_affinities.txt lbp_stage1_affinities.txt
> late_fusion.py ac_stage2_affinities.txt lbp_stage2_affinities.txt

Each resulting file are used in the second command of the steps 2.1 and 2.2, replacing the stage1_affinities.txt and stage2_affinities.txt normally used. 
