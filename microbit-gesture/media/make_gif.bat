fffmpeg -i input.mov -map_metadata -1 -c:v copy -c:a copy circle.mov
ffmpeg -i circle.mov -filter:v scale=502:-1 circle.mkv
ffmpeg -i circle.mkv -filter_complex "[0:v] palettegen" palette.png
ffmpeg -i circle.mkv -i .\palette.png -filter_complex "[0:v][1:v] paletteuse" circle.gif