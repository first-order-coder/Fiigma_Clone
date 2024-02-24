import { COLORS } from "@/constants";
import {LiveCursorProps } from "@/types/type"
import Cursor from "./Cursor";

const LiveCursors = ({ others }: LiveCursorProps) => {
    return others.map(({connectionId, presence}) => {
        if(!presence.cursor) return null;

        return (
            <Cursor
                key={connectionId}
                color={COLORS[Number(connectionId) % COLORS.length]} //will pickup random color for cursor based on connection ID
                x={presence.cursor.x}
                y={presence.cursor.y}
                message={presence.message}
            />
        )
    })
}

export default LiveCursors