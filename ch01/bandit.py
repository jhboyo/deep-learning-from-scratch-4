import numpy as np
import matplotlib.pyplot as plt


class Bandit:
    def __init__(self, arms=10):  # arms = 슬롯머신 대수
        self.rates = np.random.rand(arms)  # 슬롯머신 각각의 승률 설정(무작위)

    def play(self, arm):
        rate = self.rates[arm]
        if rate > np.random.rand():
            return 1
        else:
            return 0


class Agent:
    def __init__(self, epsilon, action_size=10):
        self.epsilon = epsilon  # 무작위로 행동할 확률(탐색 확률)
        self.Qs = np.zeros(action_size)
        self.ns = np.zeros(action_size)

    # 슬롯머신의 가치 추정
    def update(self, action, reward):
        self.ns[action] += 1
        self.Qs[action] += (reward - self.Qs[action]) / self.ns[action]

    # 행동 선택(ε-탐욕 정책)
    def get_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, len(self.Qs))  # 무작위 행동 선택
        return np.argmax(self.Qs)  # 탐욕 행동 선택


if __name__ == '__main__':
    # 실험 설정
    steps = 1000      # 총 학습 단계 수
    epsilon = 0.1     # 탐색 확률 (10% 확률로 무작위 행동)

    # 환경과 에이전트 초기화
    bandit = Bandit()       # 다중 슬롯머신 환경 생성
    agent = Agent(epsilon)  # ε-탐욕 정책 에이전트 생성
    
    # 성과 추적 변수들
    total_reward = 0        # 누적 보상 총합
    total_rewards = []      # 각 단계별 누적 보상 기록 (그래프용)
    rates = []              # 각 단계별 성공률 기록 (그래프용)

    # 강화학습 메인 루프: 에이전트가 환경과 상호작용하며 학습
    for step in range(steps):
        action = agent.get_action()   # 에이전트가 행동 선택 (ε-탐욕 정책)
        reward = bandit.play(action)  # 선택한 슬롯머신에서 보상 획득
        #print(action, reward)
        
        agent.update(action, reward)  # 경험을 바탕으로 Q-value 업데이트 
        total_reward += reward        # 누적 보상 계산
        #print(total_reward)

        # 학습 진행 상황 기록 (시각화를 위해)
        total_rewards.append(total_reward)                    # 누적 보상 저장
        rates.append(total_reward / (step + 1))              # 현재까지 평균 성공률 저장

    # 최종 결과 출력
    print(f"총 누적 보상: {total_reward}")

    # [그림 1-12] 누적 보상 변화 그래프
    # 학습이 진행되면서 보상이 어떻게 누적되는지 시각화
    plt.ylabel('Total reward')
    plt.xlabel('Steps')
    plt.plot(total_rewards)
    plt.show()

    # [그림 1-13] 성공률 변화 그래프  
    # 학습이 진행되면서 성공률이 어떻게 개선되는지 시각화
    plt.ylabel('Rates')
    plt.xlabel('Steps')
    plt.plot(rates)
    plt.show()
