import pandas as pd
import warnings
warnings.filterwarnings('ignore')

from imblearn.over_sampling import BorderlineSMOTE
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam

from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.layers import Dropout

from collections import Counter

# 데이터 불러오기
df = pd.read_csv('C:\\Users\\euclid_edu5\\workspace\\3rd_project\\Project3_beer\\search\\final_train_beer_rating.csv')
df_copy = df

# 특수기호 삭제
df['스타일소분류'] = df['스타일소분류'].str.replace(pat=r'[^\w]', repl=r'', regex=True)
X = df[['Astringent', 'Body', 'Alcoholic', 'Bitter', 'Sweet', 'Sour', 'Salty', 'Fruity', 'Hoppy', 'Spices', 'Malty']]
y = df['스타일소분류']

# y를 라벨링
encoder = LabelEncoder()
encoder.fit(y)
Y_encodered = encoder.transform(y)
print(Y_encodered)

# 데이터 정규화 Min/Max
X = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))

counter = Counter(Y_encodered)
print(counter)

# SMOTE 데이터 증식
smote = BorderlineSMOTE(random_state=0, k_neighbors=1)
X_over, y_over = smote.fit_resample(X, Y_encodered)

print('SMOTE 적용 전 학습용 피처/레이블 데이터 세트: ', X.shape, Y_encodered.shape)
print('SMOTE 적용 후 학습용 피처/레이블 데이터 세트: ', X_over.shape, y_over.shape)

# 범주형 데이터로 변환
y = np_utils.to_categorical(y_over)
X_train, X_test, y_train, y_test = train_test_split(X_over, y, test_size=0.3, random_state=777)

# 스타일명 변수 지정
style_name = df.스타일소분류.unique()
style_name.tolist()

# 모델 설정하기
model = Sequential()
model.add(layers.Dense(512, input_dim=11, activation='relu'))
model.add(Dropout(rate=0.3))
model.add(layers.Dense(256, activation='relu'))
model.add(Dropout(rate=0.3))
model.add(layers.Dense(128, activation='relu'))
model.add(Dropout(rate=0.3))
model.add(layers.Dense(108, activation='softmax'))

# 모델 구성하기
model.compile(loss='categorical_crossentropy', optimizer=Adam(0.001), metrics=['acc'])

# 모델 학습하기
history = model.fit(X_train, y_train, epochs=500, batch_size=32)

# 모델 성능평가하기
scores = model.evaluate(X_test, y_test)
print('%s: %.2f%%' % (model.metrics_names[1], scores[1] * 100))

model.save('beer_model.h5')