
class Evento():

    def getAll() -> None:
        query = """
                    SELECT 
                        e.id as id,
                        eq.nome as equipamento,
                        u.nome as usuarioNome,
                        a.nome as acionamentoNome,
                        e.dataHora as dataHoraEvento
                    FROM
                        eventos AS e
                    INNER JOIN
                        usuarios AS u
                    ON 
                        u.id = e.usuarioId 
                    INNER JOIN
                        equipamentos AS eq
                    ON 
                        eq.id = e.equipamentoId 
                    INNER JOIN
                        acionamentos AS a
                    ON 
                        a.id = e.acionamentoId 
                    AND
                        a.equipamentoId = e.equipamentoId
                """
        return query

    def getById(id) -> None:
        query = """
                SELECT 
                *
            FROM
                eventos
            WHERE
                id = '{0}'
                """.format(id)
        return query

    def getByEquipamentoId(equipamentoId):
        query = """
                SELECT 
                    e.id as id,
                    eq.nome as equipamento,
                    u.nome as usuarioNome,
                    a.nome as acionamentoNome,
                    e.dataHora as dataHoraEvento
                FROM
                    eventos AS e
                INNER JOIN
                    usuarios AS u
                ON 
                    u.id = e.usuarioId 
                INNER JOIN
                    equipamentos AS eq
                ON 
                    eq.id = e.equipamentoId 
                INNER JOIN
                    acionamentos AS a
                ON 
                    a.id = e.acionamentoId 
                AND
                    a.equipamentoId = e.equipamentoId
                WHERE
                    eq.id = '${0}'
                """.format(equipamentoId)

        return query

    def create(e):
        query = """
                INSERT INTO
                    eventos
                    (
                        id,
                        usuarioId,
                        equipamentoId,
                        acionamentoId,
                        dataHora
                    )
                VALUES
                    (
                        '${0}',
                        '${1}',
                        '${2}',
                        '${3}',
                        '${4}'
                    );
                """
