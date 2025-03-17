from typing import Dict, Callable, Any

# Gera um ID único para novos itens  (3. Closure)
def generate_id(db: Dict[int, Any]) -> Callable[[], int]:
    def get_next_id() -> int:
        if not db:
            return 1
        return max(db.keys()) + 1
    return get_next_id

