from collections import deque

def fifo_page_replacement(sequence, num_frames):
    frames = []
    queue = deque()
    page_faults = 0

    print("\n=== SIMULAÇÃO FIFO ===")
    print(f"Frames disponíveis: {num_frames}\n")

    for page in sequence:

        # Página já está na memória
        if page in frames:
            print(f"Página {page:2} -> {frames} | HIT")

        else:
            page_faults += 1

            # Ainda existe espaço livre
            if len(frames) < num_frames:
                frames.append(page)
                queue.append(page)

            # Memória cheia: remove a mais antiga
            else:
                oldest = queue.popleft()

                index = frames.index(oldest)
                frames[index] = page

                queue.append(page)

            print(f"Página {page:2} -> {frames} | PAGE FAULT")

    print("\n=== RESULTADO ===")
    print(f"Total de Page Faults: {page_faults}")
    print(f"Total de Hits: {len(sequence) - page_faults}")

    return page_faults


def main():
    print("SIMULADOR FIFO - SUBSTITUIÇÃO DE PÁGINAS")

    entrada = input(
        "\nDigite a sequência de páginas separadas por espaço:\n"
    )

    sequence = list(map(int, entrada.split()))

    num_frames = int(
        input("\nDigite a quantidade de frames da RAM: ")
    )

    fifo_page_replacement(sequence, num_frames)


if __name__ == "__main__":
    main()