#ifndef QUICKSORT_CPP
#define QUICKSORT_H

void swap(int* a, int* b)
{
  int t = *a;
  *a = *b;
  *b = t;
}

int partition(int nums[], int low, int high)
{
  int i = (low - 1);
  int pi = nums[high];

  for (int j = low; j < high; ++j) {
    if (nums[j] < pi) {
      ++i;
      swap(&nums[i], &nums[j]);
    }
  }

  swap(&nums[i + 1], &nums[high]);
  return (i + 1);
}

void quicksort(int nums[], int low, int high)
{
  if (low < high) {
    int part = partition(nums, low, high);

    quicksort(nums, low, part - 1);
    quicksort(nums, part + 1, high);
  }
}

#endif