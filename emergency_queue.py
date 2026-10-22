class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2

            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = (
                    self.data[parent_index],
                    self.data[index],
                )
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if (
                left < size
                and self.data[left].urgency < self.data[smallest].urgency
            ):
                smallest = left

            if (
                right < size
                and self.data[right].urgency < self.data[smallest].urgency
            ):
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest],
                self.data[index],
            )
            index = smallest

    def insert(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("insert() requires a Patient object")

        if (
            not isinstance(patient.urgency, int)
            or isinstance(patient.urgency, bool)
            or not 1 <= patient.urgency <= 10
        ):
            raise ValueError("Urgency must be an integer from 1 to 10")

        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} (urgency: {patient.urgency})")

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        min_patient = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)

        return min_patient


# Test your MinHeap class here, including edge cases

heap = MinHeap()

heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.insert(Patient("Morgan", 2))

heap.print_heap()

next_patient = heap.peek()
print("Next patient:", next_patient.name, next_patient.urgency)

served = heap.remove_min()
print("Served:", served.name, served.urgency)

heap.print_heap()

# edge cases
print("Empty peek:", MinHeap().peek())
print("Empty removal:", MinHeap().remove_min())

single_patient_heap = MinHeap()
single_patient_heap.insert(Patient("Casey", 4))
print("Single patient removed:", single_patient_heap.remove_min().name)
print("Queue after removing single patient:", single_patient_heap.data)
