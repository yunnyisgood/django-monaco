from dataclasses import dataclass
 #여기서 두줄정도 비어놓고 클래스선언해야한다.

@dataclass
class Dataset(object):
    context: str
    fname: str
    train: str
    test: str
    id: str  # 외부에서 주입받거나, 내부에서 외부로 내보내야하는 경우 모두 str타입으로 지정
    label: str

    @property
    def context(self) -> str: return self._context # _을 넣어 접근을 제한한다

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label







