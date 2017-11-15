import os
import sys
import argparse

from extract_subject import extract_subject

sys.path.append('..')
from img_sim.img_predict import img_sim
from image_caption.CaptionGenerator import CaptionGenerator


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--img', '-i', type=str, defalut=os.path.join('..', '..', 'sample_imgs', 'test.jpg'),
                        help="input image")
    parser.add_argument('--lang', 'l', type=str, defalut='jp', choices = ['jp', 'en', 'ch'],
                        help="choose language to generate captions")
    parser.add_argument('--cnn_model_type', '-ct', type=str, choices=['ResNet', 'VGG16', 'AlexNet'],
                        help="CNN model type")
    parser.add_argument('beamsize', '-b', type=int, defalut=3,
                        help="beamsize")
    parser.add_argument('--depth_limit', '-dl', type=int, defalut=50, 
                        help="max limit of generating tokens when constructing captions")
    parser.add_argument('--gpu', '-g', type=int, defalut=-1,
                        help="GPU ID (put -1 if you don't use gpu)")
    
    args = parser.parse_args()

    caption_generator = CaptionGenerator(
                        lang=args.lang,
                        cnn_model_type=args.cnn_model_type,
                        beamsize=args.beamsize,
                        depth_limit=args.depth_limit,
                        gpu_id=args.gpu,
                    )

    
    img_model = img_sim(
                model=args.cnn_model_type,
                gpu_id=args.gpu
            )

    captions = caption_generator.generate_sentences(args.img)
    predict = img_model.get_words(args.img, num=5, lang=args.lang)
    
    for cap in captions:
        sub = extract_subject(cap['sentence'])
    
