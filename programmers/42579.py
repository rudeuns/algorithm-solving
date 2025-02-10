def solution(genres, plays):
    answer = []

    song_dict, play_dict = {}, {}

    for i, genre in enumerate(genres):
        if genre not in song_dict:
            song_dict[genre] = [(plays[i], i)]
            play_dict[genre] = plays[i]
        else:
            song_dict[genre].append((plays[i], i))
            play_dict[genre] += plays[i]

    sorted_genre = sorted(play_dict.keys(), key=lambda x: play_dict[x], reverse=True)

    for genre in sorted_genre:
        sorted_song = sorted(song_dict[genre], key=lambda x: (-x[0], x[1]))
        answer.extend([i for _, i in sorted_song[:2]])

    return answer


"""
🎯 Solved (2025.02.10)
"""
