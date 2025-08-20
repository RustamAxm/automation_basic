

def test_get_files(get_client, mocker):
    """
    In real case return Responsive is better than fast.
    we mock data Responsive FROM MOCK. - without cal request

    :param get_client:
    :param mocker:
    :return:
    """

    mock_data = """
                   MMM.           .MMM
               MMMMMMMMMMMMMMMMMMM
               MMMMMMMMMMMMMMMMMMM      _________________________________
              MMMMMMMMMMMMMMMMMMMMM    |                                 |
             MMMMMMMMMMMMMMMMMMMMMMM   | Responsive FROM MOCK.           |
            MMMMMMMMMMMMMMMMMMMMMMMM   |_   _____________________________|
            MMMM::- -:::::::- -::MMMM    |/
             MM~:~ 00~:::::~ 00~:~MM
        .. MMMMM::.00:::+:::.00::MMMMM ..
              .MM::::: ._. :::::MM.
                 MMMM;:::::;MMMM
          -MM        MMMMMMM
          ^  M+     MMMMMMMMM
              MMMMMMM MM MM MM
                   MM MM MM MM
                   MM MM MM MM
                .~~MM~MM~MM~MM~~.
             ~~~~MM:~MM~~~MM~:MM~~~~
            ~~~~~~==~==~~~==~==~~~~~~
             ~~~~~~==~==~==~==~~~~~~
                 :~==~==~==~==~~
    """
    mock_response = mocker.MagicMock()
    mock_response.text = mock_data
    mocker.patch("requests.get", return_value=mock_response)

    vals = get_client.get_cat()
    assert "FROM MOCK" in vals