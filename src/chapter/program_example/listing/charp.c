#include <math.h>
#include <sndfile.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  const uint32_t samplerate = 44100;
  const uint32_t frames = 4 * samplerate;
  SNDFILE *const file =
      sf_open("charp.wav", SFM_WRITE,
              &(SF_INFO){.format = SF_FORMAT_WAV | SF_FORMAT_PCM_16,
                         .channels = 1,
                         .samplerate = samplerate,
                         .frames = frames});

  if (file == NULL) {
    fprintf(stderr, "failed to open \"charp.wav\".\n");
    return 1;
  }

  double *const buffer = malloc(sizeof(double) * frames);

  if (buffer == NULL) {
    fprintf(stderr, "malloc failed.\n");
    sf_close(file);
    return 1;
  }

  const double pi = 3.141592653589793;
  const double max_omega = 523.25 * 2.0 * pi / samplerate;

  for (uint32_t i = 0; i < frames; i++) {
    buffer[i] = sin(max_omega * i * i / (2.0 * frames));
  }

  if (sf_write_double(file, buffer, frames) != frames) {
    fprintf(stderr, "%s\n", sf_strerror(file));
    sf_close(file);
    free(buffer);
    return 1;
  }

  sf_close(file);
  free(buffer);
  return 0;
}
