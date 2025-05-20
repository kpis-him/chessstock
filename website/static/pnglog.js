    const game = new Chess();
        var $status = $('#status')
        var $fen = $('#fen')
        var $pgn = $('#pgn')

        var wasmSupported = typeof WebAssembly === 'object' && WebAssembly.validate(Uint8Array.of(0x0, 0x61, 0x73, 0x6d, 0x01, 0x00, 0x00, 0x00));
        var stockfish = new Worker('static/stockfish1/stockfish.js');

        document.getElementById('board1').addEventListener('touchmove', function (e) {
            e.preventDefault(); // Prevent the default scrolling behavior
        }, { passive: false });


        stockfish.addEventListener('message', function (e) {
            if (e.data.startsWith('bestmove')) {
                var bestMove = e.data.split(' ')[1];
                game.move({ from: bestMove.slice(0, 2), to: bestMove.slice(2, 4), promotion: 'q' });
                board1.position(game.fen());
                update_table();
            }
        });
        var board1 = Chessboard('board1', {
            draggable: true,
            dropOffBoard: 'trash',
            sparePieces: false,
            pieceTheme: '/static/img/chesspieces/wikipedia/{piece}.png',
            position: 'start',
            onDragStart: function (source, piece) {
                if (game.game_over()) {
                    var log = console.log(game.fen())
                    return log;
                }
                if ((game.turn() === 'w' && piece.startsWith('b')) ||
                    (game.turn() === 'b' && piece.startsWith('w'))) {
                    return false;
                }
            },
            onDrop: function (source, target) {
                const move = game.move({
                    from: source,
                    to: target,
                    promotion: 'q'
                });
                if (move === null) return 'snapback';
                //console.log("Move:", move.san);
                var table = console.log("PGN", game.pgn());
                update_table();
                stockfish.postMessage('position fen ' + game.fen());
                stockfish.postMessage('go depth 15');
            },
            onSnapEnd: function () {
                board1.position(game.fen());
            },
        });
        // $('#startBtn').on('click', board1.start);
        // $('#clearBtn').on('click', board1.clear);

        // board1.log(chess.pgn());