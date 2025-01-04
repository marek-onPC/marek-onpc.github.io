from typing import Literal, Optional

from fastapi import Query


def bool_list_serializer(is_published__list: Optional[str] = Query(default="true", description="")) -> list[Literal[True, False]]:
    serialized_filters = []
    raw_filters = is_published__list.split(",")

    for raw_val in raw_filters:
        if raw_val.lower() == "true":
            serialized_filters.append(True)
        elif  raw_val.lower() == "false":
            serialized_filters.append(False)

    if len(serialized_filters) == 0:
        return [True]
    else:
        return serialized_filters
