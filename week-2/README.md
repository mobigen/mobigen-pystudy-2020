# Python Study - Week 2
@ Jaewook Oh

## Dictionary in Python 3.6+
[참고: Stackoverflow](https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6)
Python 3.6+의 딕셔너리는 이전 딕셔너리 구현보다 나은 메모리 성능을 제공한다. 
다만, 속도 측면에서 보았을 때는 그 차이가 크지는 않다.

아래의 딕셔너리로 예를 들어보자면,

```python
d = {'timmy': 'red', 'barry': 'green', 'guido': 'blue'}
```
위 딕셔너리는 기존에는 아래와 같이 [keyhash, key, value]의 값으로 저장된다.
```python
entries = [['--', '--', '--'],
           [-8522787127447073495, 'barry', 'green'],
           ['--', '--', '--'],
           ['--', '--', '--'],
           ['--', '--', '--'],
           [-9092791511155847987, 'timmy', 'red'],
           ['--', '--', '--'],
           [-6480567542315338377, 'guido', 'blue']]
```
위처럼 사용하는 대신에, Python 3.6+의 딕셔너리 데이터는 아래와 같이 보관된다.
```python
indices =  [None, 1, None, None, None, 0, None, 2]
entries =  [[-9092791511155847987, 'timmy', 'red'],
            [-8522787127447073495, 'barry', 'green'],
            [-6480567542315338377, 'guido', 'blue']]
```

entries 배열은 딕셔너리의 아이템(PyDictKeyEntry type)을 삽입된 순서대로 유지한다.
이 순서는 새 아이템이 항상 끝에 삽입되는 형식으로 유지된다. (순서가 유지됨)

indices 배열은 entries 배열의 인덱스(즉, entries 배열에서 해당 아이템의 위치를 나타내는 값)를 보관한다.
indices 배열은 해시 테이블의 역할을 하며, key가 해시되면, indices 배열에 저장되는 인덱스 중 하나가 되고,
entries를 인덱싱해서, 해당 entry를 가져온다. 
이 배열에서는 인덱스만 유지되므로, 배열의 타입은 딕셔너리의 전체 크기에 따라 달라진다.
(32/64비트 빌드 파이썬의 int8_t (1바이트) ~ int32_t/int64_t (4/8바이트))

기존 딕셔너리는 PyDictKeyEntry형의 Sparse Array를 생성했는데, dk_size 크기가 할당되었다.
성능상의 이유로 해당 배열이 2/3 * dk_size 이상으로 채워지지 못해서, 빈 공간이 많아 메모리가 낭비되었고,
빈 공간이라고 해도, 값만 없는 PyDictKeyEntry 빈 데이터(['--', '--', '--']) 가 있는 상태였다. 

따라서, PyDictKeyEntry 타입의 배열을 만드는 기존 딕셔너리가, 
int 타입의 배열인 현재 딕셔너리보다 더 많은 메모리를 요구한다는 것을 알 수 있다.

정리하자면, Python 3.6+의 딕셔너리는
메모리 측면에서는 Python 3.5에 비해 [20% 적게](https://www.slideshare.net/mariczhuck/austin-python-meetup-2017-whats-new-in-pythons-35-and-36) 사용하게 되어 향상되었다고 할 수 있으나,
속도 측면에서의 향상은 언급하기 어려울 것으로 보인다.

마지막으로 귀도 반 로섬이 Python 3.7부터는 딕셔너리가 데이터의 삽입 순서를 유지하는 것을 규칙으로 한다는 것을
확정하였다. (https://mail.python.org/pipermail/python-dev/2017-December/151283.html)
Python 3.6에서는 CPython으로 구현되었을 경우에만 딕셔너리의 데이터 삽입 순서가 유지되었지만,
Python 3.7부터는 Python 언어의 기본 Feature로 선정되어, 모든 구현체에서 유지가 된다.

