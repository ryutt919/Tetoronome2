# Tetoronome Claim Audit

Purpose: 결과 해석을 방어하기보다, 현재 결과와 선행연구가 실제로 정합하는지 판정한다.

Evidence labels:

- Direct support: 같은 동작/대상에 가깝고 같은 변수 또는 직접 대응 변수를 측정했다.
- Mechanistic support: 직접 변수는 다르지만 생체역학적 연결이 명확하다.
- Contrast evidence: 선행연구의 일반 방향과 본 결과가 다르다.
- Not supported: 기존 보고서 문장을 문헌 근거로 지지할 수 없다.

## 1. Metronome effect: C -> M

### Cadence

- Current result: cadence +4.58%, p=0.0625, n.s.; C 187.6 -> M 196.2 steps/min.
- Existing interpretation: metronome cue increased cadence.
- Audit: Supported.
- Evidence class: Direct support.
- Reason: Heiderscheit et al. used a digital audio metronome to impose altered running step rates at constant speed. This directly supports that auditory/metronome cueing can prescribe step rate in running.
- Corrected interpretation: 메트로놈 조건은 cadence를 증가시키는 방향을 보였고, 복합 조건에서는 유의한 cadence 증가가 확인되었다.

### Shock / impact proxy

- Current result: shank mean peak g +7.51%, p=0.0625, n.s.; resultant RMS +3.43%, p=0.0625, n.s.
- Existing interpretation: cadence increase should reduce impact, but this dataset showed increased impact proxy.
- Audit: Partly correct, but any claim that metronome reduced impact is contradicted by the data.
- Evidence class: Contrast evidence plus methods caution.
- Reason: Heiderscheit et al. reported that increasing step rate shortened step length, reduced braking impulse, reduced peak vertical GRF at +10%, and decreased impact transient occurrence. The present IMU proxy increased, so Heiderscheit is a contrast source, not direct support.
- Corrected interpretation: 본 연구의 IMU 기반 충격 proxy는 메트로놈 조건에서 감소하지 않았고, step-rate 증가가 loading을 낮춘다는 선행연구의 일반 경향과 다르다. 이는 짧은 적응, 개인차, metronome synchronization burden, 그리고 IMU proxy 한계로 제한해 해석해야 한다.
- Remove/downshift: "메트로놈이 충격을 줄였다", "보폭 조절 실패 시 충격이 증가한다는 Heiderscheit 근거"는 쓰지 않는다.

### Plantarflexion / push-off

- Current result: ankle mean plantarflexion peak +34.71%, p=0.125, n.s.; ankle DP/PF ROM +11.52%, p=0.0625, n.s.
- Existing interpretation: subjects matched metronome using stronger push-off.
- Audit: Not directly supported.
- Evidence class: Mechanistic support only; direct support absent.
- Reason: The measured variable is plantarflexion angle peak. It is not ankle power, plantarflexor moment, propulsive GRF, or EMG. Yong et al. supports that plantarflexed foot posture and gastrocnemius activity differ by foot-strike pattern in running. Hamner et al. supports plantarflexor contribution to propulsion. These do not prove that metronome increased push-off force in this dataset.
- Corrected interpretation: 메트로놈 조건의 plantarflexion peak 증가는 강한 push-off의 직접 증거가 아니라, ankle posture, foot placement, 또는 strike strategy 변화로 해석한다. Push-off 강화는 측정되지 않았으므로 Discussion에서는 가능성보다 낮은 수준으로 다룬다.
- Remove/downshift: "강한 push-off 보상", "지면을 뒤로 강하게 차냈다"는 직접 근거 없이 쓰지 않는다.

### Pelvis pitch/roll stability

- Current result: pitch SD -0.46%, p=1.0; roll SD +4.26%, p=0.4375.
- Existing interpretation: metronome did not clearly improve pelvis stability.
- Audit: Supported as a negative/null result.
- Evidence class: Direct data support; literature only indirect.
- Reason: RAS/metronome gait literature mainly supports spatiotemporal parameters such as cadence, velocity, stride length, and symmetry. It does not directly require pelvis pitch/roll SD improvement.
- Corrected interpretation: 메트로놈은 본 데이터에서 골반 pitch/roll SD를 명확히 개선하지 않았다. RAS 문헌의 주된 효과 범위는 spatiotemporal gait variables이므로 pelvis SD 개선을 기대하거나 단정하지 않는다.

### Step interval CV

- Current result: step interval CV +5.09%, p=1.0.
- Existing interpretation: external rhythm adaptation may increase variability in this dataset.
- Audit: Partly supported, but direct running evidence must be marked as limited.
- Evidence class: Mechanistic support / caution.
- Reason: Sensorimotor synchronization and rhythmic cueing literature supports that external cues alter temporal control. However, this does not directly prove metronome running increases CV in the present protocol.
- Corrected interpretation: 본 데이터에서는 메트로놈 조건에서 step interval CV가 감소하지 않았다. 즉시 cue synchronization 부담 또는 개인차 가능성으로 제한해 해석한다.

## 2. Taping effect: C -> T

### Shock / impact proxy

- Current result: shank mean peak g -1.77%, p=0.4375; RMS -0.86%, p=0.5625.
- Existing interpretation: taping produced slight shock reduction but mechanism is exploratory.
- Audit: Supported only as a dataset observation, not as a literature-backed mechanism.
- Evidence class: Data observation plus indirect mechanical support.
- Reason: taping literature more directly supports ROM restriction and ankle kinematic changes than shock absorption. Proprioceptive improvement is not reliably supported by Raymond et al.
- Corrected interpretation: 테이핑 조건에서 IMU shock proxy는 소폭 감소했지만 유의하지 않았다. 선행문헌으로는 충격 완화보다 ankle ROM restriction/kinematic constraint를 우선 근거로 제시한다.

### Ankle ROM / dorsiflexion

- Current result: ankle DP/PF ROM -5.36%, p=0.1562; dorsiflexion peak -4.07%, p=0.6875.
- Existing interpretation: taping restricts dorsiflexion/ROM.
- Audit: Supported.
- Evidence class: Direct or near-direct support.
- Reason: ankle taping/support literature supports restriction of ankle ROM and altered ankle kinematics.
- Corrected interpretation: 테이핑 단독 조건은 발목 sagittal ROM과 dorsiflexion peak를 낮추는 방향을 보였으며, 이는 taping의 기계적 구속 효과와 정합한다.

### Plantarflexion

- Current result: plantarflexion peak +5.78%, p=0.6875, small effect.
- Existing interpretation: taping did not produce the large metronome-like PF increase.
- Audit: Supported as a cautious contrast.
- Evidence class: Data observation; literature support limited.
- Corrected interpretation: 테이핑 단독의 PF 증가는 작고 불확실하므로 push-off 강화로 해석하지 않는다. 핵심 taping 해석은 ROM/kinematic constraint에 둔다.

### Step interval CV

- Current result: CV -10.24%, p=0.0938, n.s.; d=-0.6707.
- Existing interpretation: step consistency improved directionally, but neural/proprioceptive mechanism cannot be claimed.
- Audit: Supported.
- Evidence class: Data observation plus caution.
- Reason: Raymond et al. does not support a consistent proprioceptive acuity improvement from tape/brace.
- Corrected interpretation: 테이핑 조건에서 step interval CV는 감소 방향을 보였지만, 이를 proprioception 향상으로 설명하지 않는다. 기계적 지지, confidence, individual response, measurement variability를 가능한 설명으로 제한한다.

## 3. Combined effect: C -> T+M and T -> T+M

### Cadence

- Current result: C -> T+M cadence +4.25%, p=0.0312; T -> T+M +3.87%, p=0.0625.
- Audit: Supported.
- Corrected interpretation: 복합 조건의 가장 강한 결과는 cadence 증가이며, 이는 metronome cue의 직접 효과로 해석 가능하다.

### Shock / impact proxy

- Current result: C -> T+M peak g +3.57%, RMS +2.09%; T -> T+M peak g +5.44%, RMS +2.97%.
- Existing interpretation: taping shock-reduction direction was offset by metronome.
- Audit: Supported as data pattern, but mechanism must be downshifted.
- Corrected interpretation: 복합 조건은 shock proxy 감소 목적에는 일관된 이득을 보이지 않았다. "상쇄"는 관찰 패턴 수준으로 쓰고, 강한 착지/push-off 때문에 상쇄되었다는 인과 표현은 피한다.

### Step interval CV

- Current result: C -> T+M +4.50%, p=0.4375; T -> T+M +16.41%, p=0.0312.
- Existing interpretation: T -> T+M에서 핵심 부작용은 timing variability 증가.
- Audit: Supported by present data.
- Corrected interpretation: 테이핑 상태에서 메트로놈을 추가하면 step interval CV가 유의하게 증가했다. 이는 복합 조건의 주요 부정적 결과로 제시 가능하되, 원인은 cue synchronization burden 등으로 제한한다.

### Pelvis

- Current result: C -> T+M roll SD +16.34%, p=0.0938; T -> T+M roll SD -22.97%, p=0.5625.
- Existing interpretation: pelvis stabilization cannot be concluded.
- Audit: Supported.
- Corrected interpretation: 복합 조건에서 골반 안정화 효과는 단정할 수 없다. T -> T+M roll SD 감소는 exploratory observation으로만 남긴다.

### Ankle PF/DF

- Current result: C -> T+M plantarflexion +36.09%, dorsiflexion -8.31%; T -> T+M plantarflexion +18.96%, dorsiflexion -2.53%.
- Existing interpretation: push-off 강화 plus dorsiflexion restriction.
- Audit: Partly unsupported.
- Corrected interpretation: 복합 조건은 plantarflexion peak 증가와 dorsiflexion peak 감소 방향을 보였다. 이는 ankle posture/strategy shift와 taping-related dorsiflexion constraint의 결합으로 해석하되, push-off power 증가로 쓰지 않는다.

## 4. Methods / IMU metric claims

- Current metric: resultant acceleration RMS and acceleration-time integral proxy from shank IMU.
- Audit: Must be framed as proxy, not biomechanical impulse.
- Corrected interpretation: 본 연구의 shock/impulse 지표는 GRF 기반 impulse가 아니라 IMU resultant acceleration 기반 proxy다. 따라서 GRF literature와 직접 등치하지 않고, direction-level comparison으로만 사용한다.

