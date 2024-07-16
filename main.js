import { createBoard, playMove } from "./connect4.js";

window.addEventListener("DOMContentLoaded", () => {
  // Initialize the UI.
  const board = document.querySelector(".board");
  createBoard(board);

  const websocket = new WebSocket("ws://localhost:8001/");
  sendMoves(board, websocket);
});

function showMessages(message){
    setTimeout(()=>alert(message),50)
}

function receiveMoves(board,websocket){
    websocket.addEventListener('message',({data})=>{
        const event = JSON.parse(data)
        switch(data.type){
            case 'play': {
                playMove(board,event.player,event.column,event.row)
                break;
            }
            case 'win': {
                showMessages(`Player ${event.player} have won `)
                websocket.close(1000);
                break;
            }
            case 'error': {
                showMessages(event.message)    
                break;
            }
            default: 
                throw new Error('Unsupported event type ')
        }
    })
}

function sendMoves(board,websocket){
    board.addEventListener('click',({target})=>{
        const column = target.dataset.column
        if(!column) {
            debugger
            return
        }
        let event = {
            type: 'play',
            column: parseInt(column,10)
        }
        websocket.send(JSON.stringify(event))
    })
}