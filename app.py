import streamlit as st
import pandas as pd
import numpy as np
import os
from datetime import datetime
from PIL import Image,ImageFilter,ImageEnhance
# 깃 연동

def load_image(image_file) : 
    img = Image.open(image_file)
    return img 

#디렉토리와 이미지를 주면,해당 디렉토리에 이 이미지를 저장하는 함수.
def save_uploaded_file(directiory,img):
    # 1. 디렉토리가 있는지 확인하여, 없으면 만든다.
    if not os.path.exists(directiory):
        os.makedirs(directiory)
    #2. 이제는 디렉토리가 있으니까 파일을 저장하라.
    filename =datetime.now().isoformat().replace(':','-').replace('.','-')
    img.save(directiory+'/'+filename+'.jpg')
    return st.success("Saved file : {} in {}".format(filename+'.jpg' , directiory))


def main() :
    
    # image_file = st.file_uploader("Upload Image", type=["png","jpg",'jpeg'])
    # img = load_image(image_file)

    image_file_list = st.file_uploader("이미지 파일 업로드",type=['png','jpeg','jpg'], accept_multiple_files=True)

    print(image_file_list)

    if image_file_list is not None :
        
        #각 파일을 이미지로 바꿔줘야 한다. (지금은 이미지파일이 아니니까)
        image_list = []

        #2-1. 모든 파일이, Image_list에 이미지로 저장됨.
        for img_file in image_file_list:
            img = load_image(img_file)
            image_list.append(img)

        #3. 화면에 출력해준다.
        for img in image_list :
            st.image(img)


    #     img = load_image(img_file)


    # #     for img_file in image_file:
    # #         img = load_image(img_file)
    # #         st.image(img,width=150)

    # # # img = Image.open('data/birds.jpg')
    # # # st.image(img)

        option_list =['Show Image','Rotate Image','Create Thumbnail','Crop Image','Merge Images',
        'Flip Image','Black & White','Filters - Sharpen','Filters - Edge Enhance',
        'Contrast Image']

        option = st.selectbox("옵션을 선택하세요.",option_list)

        if option == 'Show Image' :
            for img in image_list:
                st.image(img)

            directory = st.text_input("파일 경로 입력")
            if st.button("파일 저장") :
                #.파일 저장. 그리고 호출해줌.
                for img in image_list:
                    save_uploaded_file(directory,img)    


        elif option == 'Rotate Image' :
            #유저가 입력
            number = st.number_input('몇 도를 회전 하시겠습니까?',0,360)
            #모든 이미지를 돌려보자. 그리고 저장해보자.
            
            
            transformed_img_list =[]
            for img in image_list:
                rotated_img = img.rotate(number)
                st.image(rotated_img)
                transformed_img_list.append(rotated_img)


            directory = st.text_input("파일 경로 입력")
            if st.button("파일 저장") :
                #.파일 저장. 그리고 호출해줌.
                for img in transformed_img_list:
                    save_uploaded_file(directory,img) 



                # img = load_image(img)       
                # rotated_img = img.rotate(number)
                # # img.save("data/rot.jpg")
                # st.image(rotated_img)
                # rotated_list.append(load_image(rotated_img))


        #     if st.button('이미지 저장하기') :    
        #         for i in range(len(rotated_list)):
        #             save_uploaded_file('temp_files',rotated_list[i])


        
        #     if st.button('이미지 저장하기') :    
        #             os.path.basename()
        #             rotated_img.save('img.jpg')
            
            


        elif option == 'Create Thumbnail' :
            #가장 작은 이미지를 찾아보자

            # for img in image_list:

            number1 = st.number_input('가로의 길이를 지정해주세요',1,100)
            number2 = st.number_input('세로의 길이를 지정해주세요',1,100)
            size = (number1,number2)
            thumbnail_list = []

            for img in image_list:     
                img.thumbnail(size)
                st.image(img)
                thumbnail_list.append(img)

            directory = st.text_input("파일 경로 입력")
            if st.button("파일 저장") :
                #.파일 저장. 그리고 호출해줌.
                for img in thumbnail_list:
                    save_uploaded_file(directory,img) 

        # elif option == 'Crop Image' :
                
        #     for img in image_file: 
        #         img = load_image(img)    
        #         start_x = st.number_input('시작할 X좌표',0,img.size[0]-1)
        #         start_y = st.number_input('시작할 Y좌표',1,img.size[1]-1)
        #         max_width = img.size[0] - start_x
        #         max_height = img.size[1] - start_y
        #         width = st.number_input('width 입력',1,max_width)
        #         height = st.number_input('height 입력',1,max_height)
                
        #         box = (start_x,start_y,start_x + width,start_y + height) #시작점과 너비 깊이를 사용자에게 받아라
        #         st.write(box)
        #         cropped_img = img.crop(box)
        #         # cropped_img.save('data/crop.png')
        #         st.image(cropped_img)

        # elif option == 'Merge Images' :
        #     merge_file = st.file_uploader("Upload Image", type=["png","jpg",'jpeg'],key='merges')
        #     for img in image_file: 
        #         img = load_image(img) 

        #         if merge_file is not None:

        #             merged_img = load_image(merge_file)

        #             start_x = st.number_input('시작할 X좌표',0,img.size[0]-1)
        #             start_y = st.number_input('시작할 Y좌표',0,img.size[1]-1)

        #             position = (start_x,start_y)
        #             img.paste(merged_img,position)
        #             st.image(img)

        elif option == 'Flip Image' :
            status = st.radio('플립을 선택하세요.',['좌우반전','상하반전'])
            transformed_img_list =[]
            if status == '좌우반전':
                
                for img in image_list:
                    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)
    
            elif status == '상하반전':
                for img in image_list:
                    flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)

            directory = st.text_input("파일 경로 입력")
            if st.button("파일 저장") :
                #.파일 저장. 그리고 호출해줌.
                for img in transformed_img_list:
                    save_uploaded_file(directory,img)

        # elif option == 'Black & White' :
            
        #     covert_list =['Balck&White(1)','Color(RGB)','Gray Scale(L)']
        #     status = st.radio('플립을 선택하세요.',covert_list)
            
        #     for img in image_file: 
        #         img = load_image(img)
        #         if status == 'Balck&White(1)':
        #             bw = img.convert('1')
        #             st.image(bw)
        #         elif status == 'Color(RGB)':
        #             bw = img.convert('RGB')
        #             st.image(bw)
        #         elif status == 'Gray Scale(L)':
        #             bw = img.convert('L')
        #             st.image(bw)       
        

        # elif option == 'Filters - Sharpen' :
        #     sharp_img = img.filter(ImageFilter.SHARPEN)
        #     st.image(sharp_img)

        # elif option == 'Filters - Edge Enhance' :
        #     edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
        #     st.image(edge_img)


        # elif option == 'Contrast Image' :
        #     enhance_bar = st.slider("enhance",-20,20)
        #     contrast_img = ImageEnhance.Contrast(img).enhance(enhance_bar)
        #     st.image(contrast_img)

if __name__ == '__main__' :
    main()


#이미지를 내가 마음대로 올릴 수 있는가?(일단 한 장 해보십시오)
#하드 코딩 된 코드를 , 유저한테 입력 받아서 처리할 수 있도록 바꾼다. 



