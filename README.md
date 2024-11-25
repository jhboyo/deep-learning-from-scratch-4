# 『밑바닥부터 시작하는 딥러닝 ❹』<br>: 이번엔 강화 학습이다!

<a href="http://www.yes24.com/Product/Goods/72173703"><img src="https://github.com/WegraLee/deep-learning-from-scratch-4/blob/master/cover.jpeg" width="150" align=right></a>

**강화 학습 핵심 이론부터 문제 풀이, 심층 강화 학습까지 한 권에!**

이 책의 특징은 제목 그대로 ‘밑바닥부터 만들어가는 것’입니다. 속을 알 수 없는 외부 라이브러리에 의존하지 않고 강화 학습 알고리즘을 처음부터 구현하면서 배웁니다. 그림으로 원리를 이해하고 수학으로 강화 학습 문제를 풀어본 다음, 코드로 구현해 배운 내용을 되짚어봅니다. 코드는 최대한 간결하면서도 강화 학습에서 중요한 아이디어가 명확하게 드러나도록 짰습니다. 단계적으로 수준을 높이면서 다양한 문제에 접할 수 있도록 구성하였으니 강화 학습의 어려움과 재미를 모두 느낄 수 있을 것입니다.


[미리보기](https://preview2.hanbit.co.kr/books/yyxd/#p=1) | [알려진 오류(정오표)](https://docs.google.com/document/d/1fsPVXyPF0gpmN57VV6k0uxMfWXUbiQCwno8vCTYpMc8/edit) | [본문 그림과 수식 이미지 모음](https://github.com/WegraLee/deep-learning-from-scratch-4/blob/master/equations_and_figures_4.zip?raw=true)

---

## 파일 구성

|폴더 이름 |설명                         |
|:--        |:--                          |
|ch01       |1장에서 사용하는 소스 코드 |
|...        |...                          |
|ch09       |9장에서 사용하는 소스 코드    |
|common     |공통으로 사용하는 소스 코드   |
|notebooks  |주피터 노트북 형태의 소스 코드 |
|pytorch    |파이토치용으로 포팅된 소스 코드  |

## 주피터 노트북
이 책의 코드는 주피터 노트북으로도 제공됩니다. 다음 표의 링크를 클릭하면 구글과 캐글 같은 클라우드 서비스에서 노트북을 실행할 수 있습니다.

| 장 | Colab | 캐글 | Studio Lab |
| :--- | :--- | :--- | :--- |
| 1장 밴디트 문제| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/01_bandit.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/01_bandit.ipynb) | [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/01_bandit.ipynb) |
| 4장 동적 프로그래밍 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/04_dynamic_programming.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/04_dynamic_programming.ipynb) | [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/04_dynamic_programming.ipynb) |
| 5장 몬테카를로법 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/05_montecarlo.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/05_montecarlo.ipynb) | [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/05_montecarlo.ipynb) |
| 6장 TD법 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/06_temporal_difference.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/06_temporal_difference.ipynb) | [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/06_temporal_difference.ipynb) |
| 7장 신경망과 Q 러닝 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/07_neural_networks.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/07_neural_networks.ipynb) | [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/06_temporal_difference.ipynb) | [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/07_neural_networks.ipynb) |
| 8장 DQN | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/08_dqn.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/08_dqn.ipynb) | [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/08_dqn.ipynb) |
| 9장 정책 경사법  | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/09_policy_gradient.ipynb) | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/09_policy_gradient.ipynb) | [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/oreilly-japan/deep-learning-from-scratch-4/blob/master/notebooks/09_policy_gradient.ipynb) |


## 요구사항
소스 코드를 실행하려면 아래의 소프트웨어가 설치되어 있어야 합니다.

* 파이썬 3.x
* NumPy
* Matplotlib
* OpenAI Gym
* DeZero (혹은 파이토치)
 
이 책은 딥러닝 프레임워크로 DeZero를 사용합니다. DeZero는 시리즈 3편에서 만든 프레임워크입니다('pip install dezero' 명령으로 설치할 수 있습니다).

파이토치를 사용한 구현은 [pytorch 디렉터리](https://github.com/WegraLee/deep-learning-from-scratch-4/tree/master/pytorch)에서 제공합니다.

## 실행 방법

예제 코드들은 장별로 나눠 저장되어 있습니다. 실행하려면 다음과 같이 파이썬 명령을 실행하세요.

```
$ python ch01/avg.py
$ python ch08/dqn.py

$ cd ch09
$ python actor_critic.py
```

보다시피 각 디렉터리로 이동 후 실행해도 되고, 상위 디렉터리에서 ch0x 디렉터리를 지정해 실행해도 됩니다.

---

## 팬픽 - 바닷속 딥러닝 어드벤처 (5부작)

<img src="https://github.com/WegraLee/deep-learning-from-scratch-5/blob/main/posters/%E1%84%87%E1%85%A1%E1%84%83%E1%85%A1%E1%86%BA%E1%84%89%E1%85%A9%E1%86%A8%20%E1%84%83%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A5%E1%84%82%E1%85%B5%E1%86%BC%20%E1%84%8B%E1%85%A5%E1%84%83%E1%85%B3%E1%84%87%E1%85%A6%E1%86%AB%E1%84%8E%E1%85%A5.png?raw=true">

바닷속 세계를 배경으로, 해양 생물들이 자신의 특성과 필요에 맞는 딥러닝 기술을 개발하여 문제를 해결해 나가는 모험을 그린 연작 소설입니다. 《밑바닥부터 시작하는 딥러닝》 시리즈를 읽으신 분은 더 많은 재미를 느끼실 수 있도록 딥러닝 요소들을 곳곳에 삽입하였습니다.

각 편의 주인공과 주제는 다음과 같습니다.

1. **시야를 찾아서**: 쏨뱅이(쏨)가 **이미지 처리 기술**을 개발하여 주변 환경을 선명하게 파악
1. **상어공주**: 괭이상어 공주(꽹)가 **자연어 처리** 기술로 돌고래 왕자와의 사랑을 쟁취
1. **DeZero의 창조자**: 나뭇잎해룡(잎룡)이 **딥러닝 프레임워크**를 만들어 기술 보급과 협업 촉진
1. **제발, 가즈아!**: 가자미(가즈아)가 **심층 강화 학습**으로 먹이가 풍부한 새로운 바다 개척
1. **피쉬카소와 천재의 초상**: 유령실고기(피쉬카소)가 **이미지 생성 모델**로 바닷속 예술계 혁신

<a href="https://www.hanbit.co.kr/channel/series/series_detail_list.html?hcs_idx=34" target="_blank" rel="noopener noreferrer">소설 보러 가기</a>

---

## 라이선스

이 저장소의 소스 코드는 [MIT 라이선스](http://www.opensource.org/licenses/MIT)를 따릅니다.
상업적 목적으로도 자유롭게 이용하실 수 있습니다.
