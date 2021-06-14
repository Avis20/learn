from sys import audit

import librosa

if __name__ == '__main__':
    f_name = "/home/avis/learn/python/from_work_video/ex_numpy/32_bit_float.WAV"
    # sr = simple rate
    audio_native, sr = librosa.load(f_name, sr=48000, mono=False)
    print(
        f'кол-во каналов=[{len(audio_native)}]',
        f'type=[{type(audio_native)}]',
        f'dtype=[{audio_native.dtype}]',
        f'shape[{audio_native.shape}]',
        f'\n'
        f'кол-во измерений=[{audio_native.ndim}]',
        f'полный размер=[{audio_native.size}]',
        f'размер одного эл=[{audio_native.itemsize}]',
        sep='; '
    )

    left, right = audio_native
    print(left.shape, left.size, left)
    print(right.shape, right.size, right)

    # вытаскиваем данные обычным способом
    frames = zip(left, right)
    print(next(frames))
    print(next(frames))
    print('Срез = ')

    # через numpy срез
    # : - взять все из 1-го столбца
    frame_1 = audio_native[:, 0]
    print(frame_1)
    # в обычно было бы [0][0]
    print('Первый эл=', audio_native[0, 0])
