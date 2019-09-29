# CT Image Recognition by keras-faster RCNN by Transfering Learning
## 透過遷移學習 由keras-faster RCNN 訓練模型 由於 h5 權重檔過大 可至dropbox下載( https://www.dropbox.com/home/h5%20file )
## Kears-FRCNN: https://github.com/yhenon/keras-frcnn/
## 此方法配合 Kafka 是為了使資料能傳至已架設好的flask web, 依照以下步驟使用:

### 1.先安裝所需套件 
  pip install -r requirements.txt 

### 2.此程式已CMD下指令 (因為現在只有batch檔 只有window版本, shell on going)
  turn on CMD(CLI) and use

### 3.在CMD下先移動到此目錄位置
  cd ./keras-frcnn-master

### 4.先打開KAFKA Consumer 讓他在後台不斷runing (KAFKA安裝和使用請看另一份)
  python Consumer_img.py

### 5.for demo)如果想自行DEMO 將照片上傳並辨識 請加上此步驟
  python producer.py
   
### 6.如果你已有來源(如flask web)則開啟下方bat檔(包含producer_CT_recog.py+test_frcnn.py+img_upload.py 路徑要做更改)
  recognition.bat


# keras-frcnn
Keras implementation of Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks.
cloned from https://github.com/yhenon/keras-frcnn/

Please note that I currently am quite busy with other projects and unfortunately dont have a lot of time to spend on this maintaining this repository, but any contributions are welcome!


USAGE:
- Both theano and tensorflow backends are supported. However compile times are very high in theano, and tensorflow is highly recommended.
- `train_frcnn.py` can be used to train a model. To train on Pascal VOC data, simply do:
`python train_frcnn.py -p /path/to/pascalvoc/`. 
- the Pascal VOC data set (images and annotations for bounding boxes around the classified objects) can be obtained from: http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar
- simple_parser.py provides an alternative way to input data, using a text file. Simply provide a text file, with each
line containing:

    `filepath,x1,y1,x2,y2,class_name`

    For example:

    /data/imgs/img_001.jpg,837,346,981,456,cow
    
    /data/imgs/img_002.jpg,215,312,279,391,cat

    The classes will be inferred from the file. To use the simple parser instead of the default pascal voc style parser,
    use the command line option `-o simple`. For example `python train_frcnn.py -o simple -p my_data.txt`.

- Running `train_frcnn.py` will write weights to disk to an hdf5 file, as well as all the setting of the training run to a `pickle` file. These
settings can then be loaded by `test_frcnn.py` for any testing.

- test_frcnn.py can be used to perform inference, given pretrained weights and a config file. Specify a path to the folder containing
images:
    `python test_frcnn.py -p /path/to/test_data/`
- Data augmentation can be applied by specifying `--hf` for horizontal flips, `--vf` for vertical flips and `--rot` for 90 degree rotations



NOTES:
- config.py contains all settings for the train or test run. The default settings match those in the original Faster-RCNN
paper. The anchor box sizes are [128, 256, 512] and the ratios are [1:1, 1:2, 2:1].
- The theano backend by default uses a 7x7 pooling region, instead of 14x14 as in the frcnn paper. This cuts down compiling time slightly.
- The tensorflow backend performs a resize on the pooling region, instead of max pooling. This is much more efficient and has little impact on results.


Example output:

![ex1](http://i.imgur.com/7Lmb2RC.png)
![ex2](http://i.imgur.com/h58kCIV.png)
![ex3](http://i.imgur.com/EbvGBaG.png)
![ex4](http://i.imgur.com/i5UAgLb.png)

ISSUES:

- If you get this error:
`ValueError: There is a negative shape in the graph!`    
    than update keras to the newest version

- This repo was developed using `python2`. `python3` should work thanks to the contribution of a number of users.

- If you run out of memory, try reducing the number of ROIs that are processed simultaneously. Try passing a lower `-n` to `train_frcnn.py`. Alternatively, try reducing the image size from the default value of 600 (this setting is found in `config.py`.
